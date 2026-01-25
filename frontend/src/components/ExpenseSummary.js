// function ExpenseSummary({ expenses }) {
//   // Step 1: Calculate total expenses
//   let total = 0;

//   // Step 2: Group expenses by category
//   const categoryTotals = {};

//   expenses.forEach((expense) => {
//     total += expense.amount;

//     if (categoryTotals[expense.category]) {
//       categoryTotals[expense.category] += expense.amount;
//     } else {
//       categoryTotals[expense.category] = expense.amount;
//     }
//   });

//   return (
//     <div>
//       <h2>Expense Summary</h2>

//       <p><strong>Total Spent:</strong> {total}</p>

//       <h3>Category-wise Totals</h3>

//       {Object.keys(categoryTotals).length === 0 ? (
//         <p>No expenses to summarize.</p>
//       ) : (
//         <ul>
//           {Object.entries(categoryTotals).map(([category, amount]) => (
//             <li key={category}>
//               {category}: {amount}
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// }

// export default ExpenseSummary;

function ExpenseSummary({ expenses }) {
  let total = 0;
  const categoryTotals = {};

  expenses.forEach((e) => {
    total += e.amount;
    categoryTotals[e.category] =
      (categoryTotals[e.category] || 0) + e.amount;
  });

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-success text-white">
        Expense Summary
      </div>

      <div className="card-body">
        <h5>
          Total Spent:{" "}
          <span className="fw-bold">{total}</span>
        </h5>

        <hr />

        {Object.keys(categoryTotals.map || {}).length === 0 ? (
          <p className="text-muted">No data available</p>
        ) : (
          <ul className="list-group">
            {Object.entries(categoryTotals).map(
              ([cat, amt]) => (
                <li
                  key={cat}
                  className="list-group-item d-flex justify-content-between"
                >
                  <span>{cat}</span>
                  <span className="fw-bold">{amt}</span>
                </li>
              )
            )}
          </ul>
        )}
      </div>
    </div>
  );
}

export default ExpenseSummary;
