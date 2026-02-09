from app.extensions import get_db
from flask import current_app
import pandas as pd
from sklearn.cluster import KMeans

def spending_clusters():
    db = get_db(current_app)
    rows = db.execute("SELECT category, amount FROM expenses").fetchall()

    if not rows:
        return []

    df = pd.DataFrame(rows, columns=["category", "amount"])

    pivot = df.groupby("category")["amount"].mean().reset_index()

    if len(pivot) < 3:
        return pivot.to_dict(orient="records")

    kmeans = KMeans(n_clusters=3, n_init=10)
    pivot["cluster"] = kmeans.fit_predict(pivot[["amount"]])

    return pivot.to_dict(orient="records")
