# from app.extensions import get_db
# from flask import current_app
# import pandas as pd
# import joblib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# import pickle
# import numpy as np

# def train_category_model():
#     db = get_db(current_app)
#     rows = db.execute("SELECT title, category FROM expenses").fetchall()

#     if not rows:
#         raise ValueError("No training data in database")

#     df = pd.DataFrame(rows, columns=["title", "category"])

#     X = df["title"]
#     y = df["category"]

#     vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
#     X_vec = vectorizer.fit_transform(X)

#     model = LogisticRegression(max_iter=1000, class_weight="balanced")
#     model.fit(X_vec, y)

#     joblib.dump(model, "app/ml/model.pkl")
#     joblib.dump(vectorizer, "app/ml/vectorizer.pkl")


# def predict_category(text):
#     model = joblib.load("app/ml/model.pkl")
#     vectorizer = joblib.load("app/ml/vectorizer.pkl")

#     vec = vectorizer.transform([text])
#     return model.predict(vec)[0]



# with open("app/ml/model.pkl", "rb") as f:
#     model = pickle.load(f)

# def predict_next_month(monthly_df):
#     X = np.array(monthly_df["amount"]).reshape(-1, 1)
#     pred = model.predict(X[-3:])
#     return float(pred.mean())


import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle


# ================= TRAIN CATEGORY MODEL =================
def train_category_model(training_data):
    """
    training_data = list of dicts
    Example:
    [
        {"title": "KFC dinner", "category": "Food"},
        {"title": "Amazon order", "category": "Shopping"}
    ]
    """

    if not training_data:
        raise ValueError("No training data provided")

    df = pd.DataFrame(training_data)

    X = df["title"]
    y = df["category"]

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_vec, y)

    joblib.dump(model, "app/ml/model.pkl")
    joblib.dump(vectorizer, "app/ml/vectorizer.pkl")


# ================= PREDICT CATEGORY =================
def predict_category(text):
    model = joblib.load("app/ml/model.pkl")
    vectorizer = joblib.load("app/ml/vectorizer.pkl")

    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


# # ================= FORECAST NEXT MONTH SPENDING =================
# with open("app/ml/model.pkl", "rb") as f:
#     model = pickle.load(f)

# def predict_next_month(monthly_df):
#     X = np.array(monthly_df["amount"]).reshape(-1, 1)
#     pred = model.predict(X[-3:])
#     return float(pred.mean())

# ================= FORECAST SPENDING MODEL =================
# Load forecast model separately

# ================= FORECAST NEXT MONTH SPENDING =================
def predict_next_month(monthly_df):
    """
    Safe fallback forecast using recent average.
    Replace with ML model later.
    """

    if monthly_df is None or len(monthly_df) == 0:
        return 0.0

    recent = monthly_df["amount"].tail(3)
    return float(recent.mean())
