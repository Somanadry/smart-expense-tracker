# from app.models import Expense
# from app import db
# import pandas as pd
# from app.ml.expense_model import predict_next_month
# from app.ml.behavior_analysis import analyze_behavior
# from app.ml.anomaly import detect_anomalies



# def generate_ml_insights():

#     expenses = Expense.query.all()
#     if not expenses:
#         return {"error": "No expense data"}

#     df = pd.DataFrame([{
#         "amount": e.amount,
#         "category": e.category,
#         "date": e.date
#     } for e in expenses])

#     df['date'] = pd.to_datetime(df['date'])
#     df['month'] = df['date'].dt.to_period("M")

#     monthly = df.groupby("month")["amount"].sum().reset_index()

#     total_spent = float(df["amount"].sum())
#     top_category = df.groupby("category")["amount"].sum().idxmax()

#     prediction = predict_next_month(monthly)

#     trend, risk, recommendation = analyze_behavior(monthly, prediction)

#     chart_data = monthly.astype(str).to_dict(orient="records")

#     return {
#         "total_spent": total_spent,
#         "top_spending_category": top_category,
#         "spending_trend": trend,
#         "next_month_prediction": prediction,
#         "risk_level": risk,
#         "savings_recommendation": recommendation,
#         "chart_data": chart_data
#     }
from app.models import Expense
import pandas as pd
from app.ml.expense_model import predict_next_month
from app.ml.behavior_analysis import analyze_behavior
from app.ml.anomaly import detect_anomalies


def generate_ml_insights():

    expenses = Expense.query.all()
    if not expenses:
        return {"error": "No expense data"}

    df = pd.DataFrame([{
        "amount": e.amount,
        "category": e.category,
        "date": e.date
    } for e in expenses])

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period("M")

    monthly = df.groupby("month")["amount"].sum().reset_index()

    total_spent = float(df["amount"].sum())
    top_category = df.groupby("category")["amount"].sum().idxmax()

    prediction = predict_next_month(monthly)

    trend, base_risk, recommendation = analyze_behavior(monthly, prediction)

    anomalies = detect_anomalies(df)

    risk = base_risk.capitalize()
    if anomalies:
        risk = "High"

    # chart_data = monthly.astype(str).to_dict(orient="records")
    monthly["month"] = monthly["month"].dt.strftime("%b")
    monthly["spent"] = monthly["amount"].astype(float)

    chart_data = monthly[["month", "spent"]].to_dict(orient="records")


    # return {
    #     "total_spent": total_spent,
    #     "top_spending_category": top_category,
    #     "spending_trend": trend,
    #     "next_month_prediction": prediction,
    #     "risk_level": risk,
    #     "savings_recommendation": recommendation,
    #     "anomalies": anomalies,
    #     "chart_data": chart_data
    # }
    return {
    "total_spent": total_spent,
    "top_spending_category": top_category,
    "spending_trend": trend,
    "next_month_prediction": float(prediction),
    "risk_level": risk,
    "savings_recommendation": recommendation,
    "anomalies": anomalies,
    "chart_data": chart_data
}
