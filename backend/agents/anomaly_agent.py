from utils.config import LOW_USAGE_THRESHOLD, HIGH_COST_THRESHOLD

def detect_anomalies(df):
    anomalies = []

    for _, row in df.iterrows():
        if row["usage"] < LOW_USAGE_THRESHOLD:
            anomalies.append({
                "resource_id": row["resource_id"],
                "issue": "Low Usage",
                "cost": row["cost"],
                "severity": "High" if row["cost"] > HIGH_COST_THRESHOLD else "Medium"
            })

    return anomalies