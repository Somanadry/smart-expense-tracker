export default function PredictionCard({ value }) {
  return (
    <div className="card bg-light shadow-sm p-3">
      <h6>Next Month Prediction</h6>
      <h2>₹{value}</h2>
      <small>Based on historical spending</small>
    </div>
  );
}
