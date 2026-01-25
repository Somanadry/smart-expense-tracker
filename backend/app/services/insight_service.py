import os
def generate_insights(month, monthly_data, category_totals):
    insights = []

    total = monthly_data["total_spent"]

    if total == 0:
        return ["No spending data available for this month."]

    # 1. Category dominance
    for category, amount in category_totals.items():
        percent = round((amount / total) * 100, 1)
        if percent >= 40:
            insights.append(
                f"{category} accounts for {percent}% of your total spending this month."
            )

    # 2. High discretionary spending
    discretionary = category_totals.get("Food", 0) + category_totals.get("Entertainment", 0)
    discretionary_percent = round((discretionary / total) * 100, 1)

    if discretionary_percent >= 60:
        insights.append(
            f"Food and Entertainment together make up {discretionary_percent}% of your expenses. "
            f"Reducing them by 10% could save around {round(discretionary * 0.1, 2)}."
        )

    # 3. Spending intensity
    avg = monthly_data["average_per_day"]
    insights.append(
        f"Your average spending per active day is {avg}."
    )

    return insights

def generate_ai_insight(expenses):
    """
    Simulates sending expenses to an AI model.
    Uses placeholder API key (assignment requirement).
    """

    AI_API_KEY = os.getenv("AI_API_KEY")  # DO NOT hardcode

    if not expenses:
        return "No expenses available to analyze."

    total = sum(e["amount"] for e in expenses)

    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

    top_category = max(category_totals, key=category_totals.get)

    insight = (
        f"You spent a total of {total:.2f}. "
        f"Most of your spending is in the {top_category} category. "
        f"Reducing expenses in this category could help you save more money."
    )

    return insight
