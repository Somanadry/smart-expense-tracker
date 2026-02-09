from app.extensions import get_db
from flask import current_app
import pandas as pd

def detect_anomalies():
    db = get_db(current_app)

    rows = db.execute("SELECT amount, date FROM expenses").fetchall()

    if not rows:
        return []

    df = pd.DataFrame(rows, columns=["amount", "date"])

    std = df["amount"].std()

    if std == 0:
        return []

    df["z_score"] = (df["amount"] - df["amount"].mean()) / std
    anomalies = df[df["z_score"].abs() > 2]

    return anomalies.to_dict(orient="records")
