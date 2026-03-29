import React, { useState, useEffect } from "react";
import { Bar, Line } from "react-chartjs-2";
import "chart.js/auto";

function App() {
  const [data, setData] = useState(null);

  const runAI = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/monitor");
      const json = await res.json();
      setData(json);
    } catch (err) {
      console.error("Backend not running");
    }
  };

  useEffect(() => {
    runAI();
    const interval = setInterval(runAI, 4000);
    return () => clearInterval(interval);
  }, []);

  const barData = data
    ? {
        labels: ["Monthly", "Yearly"],
        datasets: [
          {
            label: "Savings ₹",
            data: [
              data.impact.monthly_savings,
              data.impact.yearly_savings,
            ],
          },
        ],
      }
    : null;

  const lineData = data
    ? {
        labels: data.history.map(h => h.time),
        datasets: [
          {
            label: "Live Savings Trend",
            data: data.history.map(h => h.monthly),
          },
        ],
      }
    : null;

  return (
    <div style={styles.container}>
      <h1>🚀 AutoCost AI</h1>
      <h3 style={{ color: "lime" }}>🟢 Live Monitoring Active</h3>

      {data && (
        <>
          {/* KPI */}
          <div style={styles.cards}>
            <div style={styles.card}>
              ₹{data.impact.monthly_savings}
              <p>Monthly</p>
            </div>
            <div style={styles.card}>
              ₹{data.impact.yearly_savings}
              <p>Yearly</p>
            </div>
            <div style={styles.card}>
              {data.impact.efficiency_gain}
              <p>Efficiency</p>
            </div>
          </div>

          {/* Charts */}
          <div style={styles.chart}>
            <h2>📊 Savings Overview</h2>
            <Bar data={barData} />
          </div>

          <div style={styles.chart}>
            <h2>📈 Live Trend</h2>
            <Line data={lineData} />
          </div>

          {/* Alerts */}
          <h2>🚨 Alerts</h2>
          {data.alerts.map((a, i) => (
            <div key={i} style={styles.alert}>{a}</div>
          ))}

          {/* SLA */}
          <h2>⏳ SLA Risks</h2>
          {data.sla_risks.map((r, i) => (
            <div key={i} style={styles.sla}>
              {r.resource_id} → ₹{r.penalty}
            </div>
          ))}

          {/* Actions */}
          <h2>⚙️ Actions</h2>
          {data.actions.map((a, i) => (
            <div key={i} style={styles.success}>{a.status}</div>
          ))}
        </>
      )}
    </div>
  );
}

export default App;

const styles = {
  container: {
    background: "#0f172a",
    minHeight: "100vh",
    color: "white",
    padding: "20px",
    fontFamily: "Segoe UI",
  },
  cards: {
    display: "flex",
    gap: "15px",
    marginBottom: "20px",
  },
  card: {
    background: "#1e293b",
    padding: "20px",
    borderRadius: "10px",
    textAlign: "center",
    flex: 1,
  },
  chart: {
    background: "#1e293b",
    padding: "20px",
    borderRadius: "10px",
    marginBottom: "20px",
  },
  alert: {
    background: "#7f1d1d",
    padding: "10px",
    margin: "5px 0",
    borderRadius: "6px",
  },
  sla: {
    background: "#92400e",
    padding: "10px",
    margin: "5px 0",
    borderRadius: "6px",
  },
  success: {
    background: "#065f46",
    padding: "10px",
    margin: "5px 0",
    borderRadius: "6px",
  },
};