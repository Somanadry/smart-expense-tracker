from flask import Blueprint, request, jsonify, current_app
from app.extensions import get_db
from app.services.insight_service import generate_insights
from app.services.insight_service import generate_ai_insight




expense_bp = Blueprint("expenses", __name__, url_prefix="/api/expenses")


@expense_bp.route("", methods=["POST"])
def add_expense():
    data = request.get_json()

    title = data.get("title")
    amount = data.get("amount")
    category = data.get("category")
    date = data.get("date")

    if not title or not amount or not category or not date:
        return jsonify({"error": "All fields are required"}), 400

    db = get_db(current_app)
    db.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (title, amount, category, date),
    )
    db.commit()

    return jsonify({"message": "Expense added successfully"}), 201
@expense_bp.route("", methods=["GET"])
def get_expenses():
    db = get_db(current_app)
    rows = db.execute(
        "SELECT id, title, amount, category, date, created_at FROM expenses ORDER BY date DESC"
    ).fetchall()

    expenses = []
    for row in rows:
        expenses.append(
            {
                "id": row["id"],
                "title": row["title"],
                "amount": row["amount"],
                "category": row["category"],
                "date": row["date"],
                "created_at": row["created_at"],
            }
        )

    return jsonify(expenses), 200

@expense_bp.route("/insights", methods=["GET"])
def ai_insights():
    db = get_db(current_app)

    rows = db.execute(
        "SELECT title, amount, category, date FROM expenses"
    ).fetchall()

    expenses = []
    for row in rows:
        expenses.append(
            {
                "title": row["title"],
                "amount": row["amount"],
                "category": row["category"],
                "date": row["date"],
            }
        )

    insight = generate_ai_insight(expenses)

    return jsonify({"insight": insight}), 200


@expense_bp.route("/categories", methods=["GET"])
def category_totals():
    db = get_db(current_app)
    rows = db.execute(
        """
        SELECT category, SUM(amount) as total
        FROM expenses
        GROUP BY category
        """
    ).fetchall()

    result = {}
    for row in rows:
        result[row["category"]] = row["total"]

    return jsonify(result), 200

@expense_bp.route("/monthly", methods=["GET"])
def monthly_summary():
    month = request.args.get("month")

    if not month:
        return jsonify({"error": "month query param required (YYYY-MM)"}), 400

    db = get_db(current_app)

    rows = db.execute(
        """
        SELECT
            category,
            SUM(amount) as total,
            COUNT(DISTINCT date) as days
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
        """,
        (month,),
    ).fetchall()

    if not rows:
        return jsonify(
            {
                "month": month,
                "total_spent": 0,
                "average_per_day": 0,
                "highest_category": None,
            }
        )

    total_spent = sum(row["total"] for row in rows)
    total_days = sum(row["days"] for row in rows)
    highest_category = max(rows, key=lambda r: r["total"])["category"]

    return jsonify(
        {
            "month": month,
            "total_spent": total_spent,
            "average_per_day": round(total_spent / total_days, 2),
            "highest_category": highest_category,
        }
    )
@expense_bp.route("/insights", methods=["GET"])
def insights():
    month = request.args.get("month")

    if not month:
        return jsonify({"error": "month query param required (YYYY-MM)"}), 400

    db = get_db(current_app)

    # Monthly summary
    rows = db.execute(
        """
        SELECT category, SUM(amount) as total
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
        """,
        (month,),
    ).fetchall()

    category_totals = {row["category"]: row["total"] for row in rows}

    total_spent = sum(category_totals.values())
    days = db.execute(
        """
        SELECT COUNT(DISTINCT date) as days
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        """,
        (month,),
    ).fetchone()["days"] or 1

    monthly_data = {
        "total_spent": total_spent,
        "average_per_day": round(total_spent / days, 2),
    }

    insights = generate_insights(month, monthly_data, category_totals)

    return jsonify(
        {
            "month": month,
            "insights": insights
        }
    )
    

    
from flask import jsonify, current_app

@expense_bp.route("/<int:expense_id>", methods=["DELETE", "OPTIONS"])
def delete_expense(expense_id):
    db = get_db(current_app)

    # Check if expense exists
    row = db.execute(
        "SELECT id FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    if not row:
        return jsonify({"error": "Expense not found"}), 404

    # Delete expense
    db.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    db.commit()

    return jsonify({"message": "Expense deleted successfully"}), 200
    # CORS(app) 