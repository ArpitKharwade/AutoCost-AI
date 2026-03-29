from utils.config import SLA_PENALTY_PER_UNIT

def detect_sla_risk(df):
    risks = []

    for _, row in df.iterrows():
        if row["task_time"] > row["sla_limit"]:
            penalty = (row["task_time"] - row["sla_limit"]) * SLA_PENALTY_PER_UNIT

            risks.append({
                "resource_id": row["resource_id"],
                "issue": "SLA Breach Risk",
                "penalty": penalty,
                "severity": "High"
            })

    return risks