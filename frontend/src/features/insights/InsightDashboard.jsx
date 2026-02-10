import { useEffect, useState } from "react";
import { fetchInsights } from "../../services/api";
import KPICards from "./KPICards";
import SpendingTrendChart from "./SpendingTrendChart";
import PredictionCard from "./PredictionCard";
import AnomalyPanel from "./AnomalyPanel";
import SavingsAdvice from "./SavingsAdvice";

export default function InsightDashboard() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchInsights()
      .then(setData)
      .catch(() => setError("AI insights failed to load"));
  }, []);

  if (error) return <p className="text-danger">{error}</p>;
  if (!data) return <p>Analyzing spending patterns...</p>;

  return (
    <>
      <KPICards data={data} />

      {data.chart_data?.length > 0 && (
        <div className="row mt-4">
          <div className="col-md-8">
            <SpendingTrendChart chartData={data.chart_data} />
          </div>
          <div className="col-md-4">
            <PredictionCard value={data.next_month_prediction} />
          </div>
        </div>
      )}

      <div className="row mt-4">
        <div className="col-md-6">
          <AnomalyPanel anomalies={data.anomalies || []} />
        </div>
        <div className="col-md-6">
          <SavingsAdvice advice={data.savings_recommendation} />
        </div>
      </div>
    </>
  );
}
