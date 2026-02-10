import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

export default function SpendingTrendChart({ chartData }) {
  if (!chartData || chartData.length === 0) {
    return <p>No trend data available</p>;
  }

  return (
    <div className="card shadow-sm p-3">
      <h6>Spending Trend</h6>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="spent" stroke="#0d6efd" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
