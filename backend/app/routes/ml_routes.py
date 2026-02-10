from flask import Blueprint, jsonify
from app.services.ml_service import generate_ml_insights

ml_bp = Blueprint("ml", __name__)

@ml_bp.route("/api/ml-insights", methods=["GET"])
def ml_insights():
    insights = generate_ml_insights()
    return jsonify(insights)
