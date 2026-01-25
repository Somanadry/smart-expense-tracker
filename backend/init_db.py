from app import create_app
from app.extensions import get_db
from app.models.expense import create_expense_table


app = create_app()

with app.app_context():
    db = get_db(app)
    create_expense_table(db)
    print("Database initialized successfully.")
