// import { useEffect, useState } from "react";
// import { fetchInsights } from "../services/api";

// function AIInsights() {
//   const [insight, setInsight] = useState("");
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const loadInsights = async () => {
//       const data = await fetchInsights();
//       setInsight(data.insight);
//       setLoading(false);
//     };

//     loadInsights();
//   }, []);

//   return (
//     <div>
//       <h2>AI Spending Insights</h2>

//       {loading ? (
//         <p>Analyzing your expenses...</p>
//       ) : (
//         <p>{insight}</p>
//       )}
//     </div>
//   );
// }

// export default AIInsights;

// import { useEffect, useState } from "react";

// function AIInsights() {
//   const [insight, setInsight] = useState("");
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const fetchInsights = async () => {
//       try {
//         const response = await fetch(
//           "http://127.0.0.1:5000/api/expenses/insights"
//         );

//         if (!response.ok) {
//           throw new Error("Failed to fetch AI insights");
//         }

//         const data = await response.json();
//         setInsight(data.insight);
//       } catch (err) {
//         setError("Unable to load AI insights at this time.");
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchInsights();
//   }, []);

//   return (
//     <div>
//       <h2>AI Spending Insights</h2>

//       {loading && <p>Analyzing your spending patterns...</p>}

//       {error && <p>{error}</p>}

//       {!loading && !error && <p>{insight}</p>}
//     </div>
//   );
// }

// export default AIInsights;

import { useEffect, useState } from "react";

function AIInsights() {
  const [insight, setInsight] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

//   useEffect(() => {
//     const load = async () => {
//       try {
//         const res = await fetch(
//           "http://127.0.0.1:5000/api/expenses/insights"
//         );
//         if (!res.ok) throw new Error();
//         const data = await res.json();
//         setInsight(data.insight);
//       } catch {
//         setError("Unable to load AI insights.");
//       } finally {
//         setLoading(false);
//       }
//     };
//     load();
//   }, []);
    useEffect(() => {
  const load = async () => {
    try {
      const now = new Date();
      const month = `${now.getFullYear()}-${String(
        now.getMonth() + 1
      ).padStart(2, "0")}`;

      const res = await fetch(
        `https://smart-expense-tracker-u5mh.onrender.com/api/expenses/insights?month=${month}`
      );

      if (!res.ok) throw new Error();

      const data = await res.json();
      setInsight(data.insight);
    } catch {
      setError("Unable to load AI insights.");
    } finally {
      setLoading(false);
    }
  };

  load();
}, []);


  return (
    <div className="card shadow-sm">
      <div className="card-header bg-info text-white">
        AI Spending Insights
      </div>

      <div className="card-body">
        {loading && <p>Analyzing spending...</p>}
        {error && <p className="text-danger">{error}</p>}
        {!loading && !error && <p>{insight}</p>}
      </div>
    </div>
  );
}

export default AIInsights;
