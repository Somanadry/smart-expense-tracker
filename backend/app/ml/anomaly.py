# from app.extensions import get_db
# from flask import current_app
# import pandas as pd

# def detect_anomalies():
#     db = get_db(current_app)

#     rows = db.execute("SELECT amount, date FROM expenses").fetchall()

#     if not rows:
#         return []

#     df = pd.DataFrame(rows, columns=["amount", "date"])

#     std = df["amount"].std()

#     if std == 0:
#         return []

#     df["z_score"] = (df["amount"] - df["amount"].mean()) / std
#     anomalies = df[df["z_score"].abs() > 2]

#     return anomalies.to_dict(orient="records")

# import pandas as pd

# def detect_anomalies(df):
#     """
#     Monthly behavioral anomaly detection using Z-score
#     """

#     if df.empty:
#         return []

#     df['date'] = pd.to_datetime(df['date'])
#     df['month'] = df['date'].dt.to_period("M")

#     monthly = df.groupby('month')['amount'].sum().reset_index()

#     std = monthly["amount"].std()
#     if std == 0 or pd.isna(std):
#         return []

#     mean = monthly["amount"].mean()
#     monthly["z_score"] = (monthly["amount"] - mean) / std

#     anomalies = monthly[monthly["z_score"].abs() > 2]

#     return anomalies.to_dict(orient="records")

import pandas as pd

def detect_anomalies(df):
    """
    Transaction-level anomaly detection using Z-score + spike rule
    """

    if df.empty:
        return []

    df["amount"] = pd.to_numeric(df["amount"])

    mean = df["amount"].mean()
    std = df["amount"].std()

    if std == 0 or pd.isna(std):
        return []

    df["z_score"] = (df["amount"] - mean) / std

    # Z-score anomalies
    z_anomalies = df[df["z_score"].abs() > 2]

    # Rule-based spike detection (important)
    spike_threshold = mean * 3
    spike_anomalies = df[df["amount"] > spike_threshold]

    anomalies = pd.concat([z_anomalies, spike_anomalies]).drop_duplicates()

    return anomalies[["date", "amount"]].to_dict(orient="records")
