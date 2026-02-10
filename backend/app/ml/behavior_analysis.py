# from app.extensions import get_db
# from flask import current_app
# import pandas as pd
# from sklearn.cluster import KMeans

# def spending_clusters():
#     db = get_db(current_app)
#     rows = db.execute("SELECT category, amount FROM expenses").fetchall()

#     if not rows:
#         return []

#     df = pd.DataFrame(rows, columns=["category", "amount"])

#     pivot = df.groupby("category")["amount"].mean().reset_index()

#     if len(pivot) < 3:
#         return pivot.to_dict(orient="records")

#     kmeans = KMeans(n_clusters=3, n_init=10)
#     pivot["cluster"] = kmeans.fit_predict(pivot[["amount"]])

#     return pivot.to_dict(orient="records")

# def analyze_behavior(monthly_df, prediction):

#     trend = "stable"
#     if len(monthly_df) >= 2:
#         last = monthly_df["amount"].iloc[-1]
#         prev = monthly_df["amount"].iloc[-2]
#         if last > prev:
#             trend = "increasing"
#         elif last < prev:
#             trend = "decreasing"

#     avg = monthly_df["amount"].mean()

#     risk = "low"
#     if prediction > avg * 1.3:
#         risk = "high"
#     elif prediction > avg:
#         risk = "medium"

#     if risk == "high":
#         rec = "Cut discretionary expenses immediately."
#     elif risk == "medium":
#         rec = "Track category budgets closely."
#     else:
#         rec = "Your spending pattern is stable."

#     return trend, risk, rec
import pandas as pd
from sklearn.cluster import KMeans


# ================= CLUSTER SPENDING PATTERNS =================
def spending_clusters(expense_data):
    """
    expense_data = list of dicts
    [
        {"category": "Food", "amount": 500},
        {"category": "Shopping", "amount": 2000}
    ]
    """

    if not expense_data:
        return []

    df = pd.DataFrame(expense_data)

    pivot = df.groupby("category")["amount"].mean().reset_index()

    if len(pivot) < 3:
        return pivot.to_dict(orient="records")

    kmeans = KMeans(n_clusters=3, n_init=10)
    pivot["cluster"] = kmeans.fit_predict(pivot[["amount"]])

    return pivot.to_dict(orient="records")


# ================= BEHAVIOR ANALYSIS =================
def analyze_behavior(monthly_df, prediction):

    trend = "stable"
    if len(monthly_df) >= 2:
        last = monthly_df["amount"].iloc[-1]
        prev = monthly_df["amount"].iloc[-2]
        if last > prev:
            trend = "increasing"
        elif last < prev:
            trend = "decreasing"

    avg = monthly_df["amount"].mean()

    risk = "low"
    if prediction > avg * 1.3:
        risk = "high"
    elif prediction > avg:
        risk = "medium"

    if risk == "high":
        rec = "Cut discretionary expenses immediately."
    elif risk == "medium":
        rec = "Track category budgets closely."
    else:
        rec = "Your spending pattern is stable."

    return trend, risk, rec
