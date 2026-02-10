# from flask import Blueprint, request, jsonify, current_app
# from app.extensions import get_db
# from app.services.insight_service import generate_insights
# from app.services.insight_service import generate_ai_insight
# from app.ml.expense_model import predict_category, train_category_model
# from app.ml.behavior_analysis import spending_clusters
# from app.ml.anomaly import detect_anomalies



# expense_bp = Blueprint("expenses", __name__, url_prefix="/api/expenses")


# @expense_bp.route("", methods=["POST"])
# def add_expense():
#     data = request.get_json()

#     title = data.get("title")
#     amount = data.get("amount")
#     category = data.get("category")
#     date = data.get("date")

#     if not title or not amount or not category or not date:
#         return jsonify({"error": "All fields are required"}), 400

#     db = get_db(current_app)
#     db.execute(
#         "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
#         (title, amount, category, date),
#     )
#     db.commit()

#     return jsonify({"message": "Expense added successfully"}), 201
# @expense_bp.route("", methods=["GET"])
# def get_expenses():
#     db = get_db(current_app)
#     rows = db.execute(
#         "SELECT id, title, amount, category, date, created_at FROM expenses ORDER BY date DESC"
#     ).fetchall()

#     expenses = []
#     for row in rows:
#         expenses.append(
#             {
#                 "id": row["id"],
#                 "title": row["title"],
#                 "amount": row["amount"],
#                 "category": row["category"],
#                 "date": row["date"],
#                 "created_at": row["created_at"],
#             }
#         )

#     return jsonify(expenses), 200

# @expense_bp.route("/insights", methods=["GET"])
# def ai_insights():
#     db = get_db(current_app)

#     rows = db.execute(
#         "SELECT title, amount, category, date FROM expenses"
#     ).fetchall()

#     expenses = []
#     for row in rows:
#         expenses.append(
#             {
#                 "title": row["title"],
#                 "amount": row["amount"],
#                 "category": row["category"],
#                 "date": row["date"],
#             }
#         )

#     insight = generate_ai_insight(expenses)

#     return jsonify({"insight": insight}), 200


# @expense_bp.route("/categories", methods=["GET"])
# def category_totals():
#     db = get_db(current_app)
#     rows = db.execute(
#         """
#         SELECT category, SUM(amount) as total
#         FROM expenses
#         GROUP BY category
#         """
#     ).fetchall()

#     result = {}
#     for row in rows:
#         result[row["category"]] = row["total"]

#     return jsonify(result), 200

# @expense_bp.route("/monthly", methods=["GET"])
# def monthly_summary():
#     month = request.args.get("month")

#     if not month:
#         return jsonify({"error": "month query param required (YYYY-MM)"}), 400

#     db = get_db(current_app)

#     rows = db.execute(
#         """
#         SELECT
#             category,
#             SUM(amount) as total,
#             COUNT(DISTINCT date) as days
#         FROM expenses
#         WHERE strftime('%Y-%m', date) = ?
#         GROUP BY category
#         """,
#         (month,),
#     ).fetchall()

#     if not rows:
#         return jsonify(
#             {
#                 "month": month,
#                 "total_spent": 0,
#                 "average_per_day": 0,
#                 "highest_category": None,
#             }
#         )

#     total_spent = sum(row["total"] for row in rows)
#     total_days = sum(row["days"] for row in rows)
#     highest_category = max(rows, key=lambda r: r["total"])["category"]

#     return jsonify(
#         {
#             "month": month,
#             "total_spent": total_spent,
#             "average_per_day": round(total_spent / total_days, 2),
#             "highest_category": highest_category,
#         }
#     )
# @expense_bp.route("/insights", methods=["GET"])
# def insights():
#     month = request.args.get("month")

#     if not month:
#         return jsonify({"error": "month query param required (YYYY-MM)"}), 400

#     db = get_db(current_app)

#     # Monthly summary
#     rows = db.execute(
#         """
#         SELECT category, SUM(amount) as total
#         FROM expenses
#         WHERE strftime('%Y-%m', date) = ?
#         GROUP BY category
#         """,
#         (month,),
#     ).fetchall()

#     category_totals = {row["category"]: row["total"] for row in rows}

#     total_spent = sum(category_totals.values())
#     days = db.execute(
#         """
#         SELECT COUNT(DISTINCT date) as days
#         FROM expenses
#         WHERE strftime('%Y-%m', date) = ?
#         """,
#         (month,),
#     ).fetchone()["days"] or 1

#     monthly_data = {
#         "total_spent": total_spent,
#         "average_per_day": round(total_spent / days, 2),
#     }

#     insights = generate_insights(month, monthly_data, category_totals)

#     return jsonify(
#         {
#             "month": month,
#             "insights": insights
#         }
#     )
    

    
# from flask import jsonify, current_app

# @expense_bp.route("/<int:expense_id>", methods=["DELETE", "OPTIONS"])
# def delete_expense(expense_id):
#     db = get_db(current_app)

#     # Check if expense exists
#     row = db.execute(
#         "SELECT id FROM expenses WHERE id = ?",
#         (expense_id,)
#     ).fetchone()

#     if not row:
#         return jsonify({"error": "Expense not found"}), 404

#     # Delete expense
#     db.execute(
#         "DELETE FROM expenses WHERE id = ?",
#         (expense_id,)
#     )
#     db.commit()

#     return jsonify({"message": "Expense deleted successfully"}), 200
#     # CORS(app) 
    
# from app.ml.expense_model import predict_category, train_category_model

# @expense_bp.route("/train-model", methods=["POST"])
# def train_model():
#     try:
#         train_category_model()
#         return jsonify({"message": "Model trained"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# @expense_bp.route("/predict-category", methods=["POST"])
# def predict():
#     text = request.json.get("title")
#     if not text:
#         return jsonify({"error": "title required"}), 400

#     pred = predict_category(text)
#     return jsonify({"predicted_category": pred})

# @expense_bp.route("/clusters", methods=["GET"])
# def clusters():
#     return jsonify(spending_clusters())

# @expense_bp.route("/anomalies", methods=["GET"])
# def anomalies():
#     return jsonify(detect_anomalies())
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Expense
from datetime import datetime
from app.services.insight_service import generate_insights, generate_ai_insight
from app.ml.expense_model import predict_category, train_category_model
from app.ml.behavior_analysis import spending_clusters
from app.ml.anomaly import detect_anomalies

expense_bp = Blueprint("expenses", __name__, url_prefix="/api/expenses")


# ---------------- ADD EXPENSE ----------------
@expense_bp.route("", methods=["POST"])
def add_expense():
    data = request.get_json()

    expense = Expense(
        title=data["title"],
        amount=float(data["amount"]),
        category=data["category"],
        date=datetime.strptime(data["date"], "%Y-%m-%d").date()
    )

    db.session.add(expense)
    db.session.commit()
    return jsonify({"message": "Expense added"}), 201


# ---------------- GET ALL ----------------
@expense_bp.route("", methods=["GET"])
def get_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()

    return jsonify([
        {
            "id": e.id,
            "title": e.title,
            "amount": e.amount,
            "category": e.category,
            "date": e.date.strftime("%Y-%m-%d"),
            "created_at": e.created_at.strftime("%Y-%m-%d %H:%M:%S") if e.created_at else None
        }
        for e in expenses
    ])


# ---------------- DELETE ----------------
@expense_bp.route("/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted"}), 200


# ---------------- AI INSIGHTS ----------------
@expense_bp.route("/ai-insights", methods=["GET"])
def ai_insights():
    expenses = Expense.query.all()

    data = [{
        "title": e.title,
        "amount": e.amount,
        "category": e.category,
        "date": e.date
    } for e in expenses]

    insight = generate_ai_insight(data)
    return jsonify({"insight": insight})


# ---------------- CATEGORY TOTALS ----------------
@expense_bp.route("/categories", methods=["GET"])
def category_totals():
    from sqlalchemy import func

    rows = db.session.query(
        Expense.category,
        func.sum(Expense.amount)
    ).group_by(Expense.category).all()

    return jsonify({cat: float(total) for cat, total in rows})


# ---------------- MONTHLY SUMMARY ----------------
@expense_bp.route("/monthly", methods=["GET"])
def monthly_summary():
    from sqlalchemy import func

    month = request.args.get("month")
    rows = db.session.query(
        Expense.category,
        func.sum(Expense.amount)
    ).filter(func.strftime("%Y-%m", Expense.date) == month)\
     .group_by(Expense.category).all()

    total_spent = sum(total for _, total in rows)

    return jsonify({
        "month": month,
        "total_spent": float(total_spent),
        "highest_category": max(rows, key=lambda r: r[1])[0] if rows else None
    })


# ---------------- MODEL TRAIN ----------------
@expense_bp.route("/train-model", methods=["POST"])
def train_model():
    train_category_model()
    return jsonify({"message": "Model trained"})


# ---------------- PREDICT CATEGORY ----------------
@expense_bp.route("/predict-category", methods=["POST"])
def predict():
    text = request.json.get("title")
    return jsonify({"predicted_category": predict_category(text)})


# ---------------- CLUSTERS ----------------
@expense_bp.route("/clusters", methods=["GET"])
def clusters():
    return jsonify(spending_clusters())


# # ---------------- ANOMALIES ----------------
# @expense_bp.route("/anomalies", methods=["GET"])
# def anomalies():
#     expenses = Expense.query.all()
#     data = [{"amount": e.amount, "date": e.date} for e in expenses]
#     return jsonify(detect_anomalies(data))

import pandas as pd

# ---------------- ANOMALIES ----------------
@expense_bp.route("/anomalies", methods=["GET"])
def anomalies():
    expenses = Expense.query.all()

    df = pd.DataFrame([{
        "amount": e.amount,
        "date": e.date
    } for e in expenses])

    if df.empty:
        return jsonify([])

    df["date"] = pd.to_datetime(df["date"])

    return jsonify(detect_anomalies(df))
