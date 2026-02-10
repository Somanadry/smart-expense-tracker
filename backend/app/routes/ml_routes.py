from flask import Blueprint, jsonify
from app.services.ml_service import generate_ml_insights
from flask_cors import cross_origin


ml_bp = Blueprint("ml", __name__)

@ml_bp.route("/api/ml-insights", methods=["GET"])
@cross_origin()
def ml_insights():
    insights = generate_ml_insights()
    return jsonify(insights)
