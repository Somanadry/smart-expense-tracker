export default function KPICards({ data }) {
  const riskColor = {
    Low: "success",
    Medium: "warning",
    High: "danger",
  }[data.risk_level] || "secondary";

  return (
    <div className="row">
      <div className="col-md-4">
        <div className="card shadow-sm">
          <div className="card-body">
            <h6>Total Spent</h6>
            <h3>₹{data.total_spent}</h3>
          </div>
        </div>
      </div>

      <div className="col-md-4">
        <div className="card shadow-sm">
          <div className="card-body">
            <h6>Top Category</h6>
            <h4>{data.top_spending_category}</h4>
          </div>
        </div>
      </div>

      <div className="col-md-4">
        <div className="card shadow-sm">
          <div className="card-body">
            <h6>Risk Level</h6>
            <span className={`badge bg-${riskColor}`}>
              {data.risk_level}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
