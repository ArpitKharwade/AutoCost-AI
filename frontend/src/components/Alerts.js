export default function Alerts({ alerts }) {
  return (
    <div>
      <h2>🚨 Alerts</h2>
      {alerts.map((a, i) => (
        <p key={i} style={{ color: "red" }}>{a}</p>
      ))}
    </div>
  );
}