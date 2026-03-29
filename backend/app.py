from flask import Flask, jsonify
from flask_cors import CORS
import time

from agents.data_agent import load_data
from agents.anomaly_agent import detect_anomalies
from agents.sla_agent import detect_sla_risk
from agents.spend_agent import detect_duplicate_costs
from agents.decision_agent import decide_actions
from agents.action_agent import execute_actions
from agents.impact_agent import calculate_impact, simulate_future
from agents.alert_agent import generate_alerts

app = Flask(__name__)
CORS(app)

# 🔥 GLOBAL HISTORY STORAGE
history = []

@app.route("/monitor", methods=["GET"])
def monitor():
    global history

    data = load_data()

    anomalies = detect_anomalies(data)
    sla_risks = detect_sla_risk(data)
    duplicates = detect_duplicate_costs(data)

    decisions = decide_actions(anomalies, sla_risks, duplicates)
    actions = execute_actions(decisions)

    impact = calculate_impact(actions)
    future = simulate_future(actions)
    alerts = generate_alerts(actions)

    # 🔥 STORE HISTORY
    history.append({
        "time": time.strftime("%H:%M:%S"),
        "monthly": impact["monthly_savings"]
    })

    # keep last 10 records only
    history = history[-10:]

    return jsonify({
        "anomalies": anomalies,
        "sla_risks": sla_risks,
        "duplicates": duplicates,
        "actions": actions,
        "impact": impact,
        "future": future,
        "alerts": alerts,
        "history": history
    })

if __name__ == "__main__":
    app.run(debug=True)