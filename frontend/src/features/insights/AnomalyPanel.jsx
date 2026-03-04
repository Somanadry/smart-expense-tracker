export default function AnomalyPanel({ anomalies }) {
  return (
    <div className="card shadow-sm p-3">
      <h6>Spending Anomalies</h6>

      {anomalies && anomalies.length > 0 ? (
        <ul className="mb-0">
          {anomalies.map((a, i) => (
            <li key={i}>
              <strong>₹{a.amount}</strong> on {new Date(a.date).toLocaleDateString()}
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-muted">No anomalies detected</p>
      )}
    </div>
  );
}
