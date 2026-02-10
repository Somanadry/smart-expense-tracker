# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)
# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from app import create_app
from app.extensions import db
from app.models import Expense  # ensures model is registered

app = create_app()

# Create tables automatically if they don’t exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
