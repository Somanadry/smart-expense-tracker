export default function SavingsAdvice({ advice }) {
  return (
    <div className="card border-success shadow-sm p-3">
      <h6>Savings Recommendation</h6>
      <p>{advice}</p>
    </div>
  );
}
