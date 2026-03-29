def calculate_impact(actions):
    total = sum(a["impact_value"] for a in actions)

    return {
        "monthly_savings": total,
        "yearly_savings": total * 12,
        "efficiency_gain": f"{min(40, int(total/1000)*5)}%"
    }

def simulate_future(actions):
    total = sum(a["impact_value"] for a in actions)
    return {
        "projected_savings": int(total * 1.2)
    }