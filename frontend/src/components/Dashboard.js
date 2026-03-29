export default function Dashboard({ data }) {
  return (
    <div>
      <h2>🔍 Detected Issues</h2>
      {data.anomalies.map((a, i) => (
        <p key={i}>{a.resource_id} → {a.issue}</p>
      ))}

      <h2>⚡ Actions Taken</h2>
      {data.actions.map((a, i) => (
        <p key={i}>{a.status}</p>
      ))}

      <h2>💰 Impact</h2>
      <p>Monthly Savings: ₹{data.impact.monthly_savings}</p>
      <p>Yearly Savings: ₹{data.impact.yearly_savings}</p>
    </div>
  );
}