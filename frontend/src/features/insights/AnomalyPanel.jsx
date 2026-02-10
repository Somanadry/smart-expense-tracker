export default function AnomalyPanel({ anomalies }) {
  return (
    <div className="card shadow-sm p-3">
      <h6>Spending Anomalies</h6>
      {anomalies.length > 0 ? (
        <ul>
          {anomalies.map((a, i) => (
            <li key={i}>{a}</li>
          ))}
        </ul>
      ) : (
        <p>No anomalies detected</p>
      )}
    </div>
  );
}
