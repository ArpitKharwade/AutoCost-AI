def decide_actions(anomalies, sla_risks, duplicates):
    decisions = []

    # anomaly decisions
    for item in anomalies:
        decisions.append({
            "resource_id": item["resource_id"],
            "action": "Shutdown",
            "reason": "Low utilization detected",
            "impact_value": item["cost"]
        })

    # SLA decisions
    for risk in sla_risks:
        decisions.append({
            "resource_id": risk["resource_id"],
            "action": "Reallocate Resources",
            "reason": f"Prevent SLA penalty ₹{risk['penalty']}",
            "impact_value": risk["penalty"]
        })

    # duplicate cost decisions
    for dup in duplicates:
        decisions.append({
            "resource_id": dup["resource_id"],
            "action": "Remove Duplicate",
            "reason": "Duplicate service detected",
            "impact_value": dup["cost"]
        })

    return decisions