def generate_alerts(actions):
    alerts = []

    for a in actions:
        alerts.append(f"{a['resource_id']} → {a['status']} → Saved ₹{a['impact_value']}")

    return alerts