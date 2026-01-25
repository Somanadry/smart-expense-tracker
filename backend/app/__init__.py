from flask import Flask
from flask_cors import CORS

from app.routes.health import health_bp
from app.routes.expense_routes import expense_bp
from app.config import Config
from app.extensions import close_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(
    app,
    resources={r"/api/*": {"origins": "*"}},
    methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type"]
)


    app.register_blueprint(health_bp)
    app.register_blueprint(expense_bp)

    app.teardown_appcontext(close_db)
    print(app.url_map)

    return app
