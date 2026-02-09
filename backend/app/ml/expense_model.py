from app.extensions import get_db
from flask import current_app
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_category_model():
    db = get_db(current_app)
    rows = db.execute("SELECT title, category FROM expenses").fetchall()

    if not rows:
        raise ValueError("No training data in database")

    df = pd.DataFrame(rows, columns=["title", "category"])

    X = df["title"]
    y = df["category"]

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_vec, y)

    joblib.dump(model, "app/ml/model.pkl")
    joblib.dump(vectorizer, "app/ml/vectorizer.pkl")


def predict_category(text):
    model = joblib.load("app/ml/model.pkl")
    vectorizer = joblib.load("app/ml/vectorizer.pkl")

    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
