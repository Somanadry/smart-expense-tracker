// function ExpenseList({ expenses }) {
//   return (
//     <div>
//       <h2>Expenses</h2>

//       <ul>
//         {expenses.map((expense) => (
//           <li key={expense.id}>
//             <strong>{expense.title}</strong> — {expense.amount} —{" "}
//             {expense.category} — {expense.date}
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default ExpenseList;

// import { deleteExpense } from "../services/api";

// function ExpenseList({ expenses, onExpenseDeleted }) {
//   const handleDelete = async (id) => {
//     await deleteExpense(id);
//     onExpenseDeleted();
//   };

//   return (
//     <div>
//       <h2>Expenses</h2>

//       <ul>
//         {expenses.map((expense) => (
//           <li key={expense.id}>
//             <strong>{expense.title}</strong> — {expense.amount} —{" "}
//             {expense.category} — {expense.date}
//             <button
//               style={{ marginLeft: "10px" }}
//               onClick={() => handleDelete(expense.id)}
//             >
//               Delete
//             </button>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default ExpenseList;
// import { deleteExpense } from "../services/api";

// function ExpenseList({ expenses, onExpenseDeleted }) {
//   const handleDelete = async (id) => {
//     await deleteExpense(id);
//     onExpenseDeleted();
//   };

//   if (expenses.length === 0) {
//     return <p>No expenses found.</p>;
//   }

//   return (
//     <div>
//       <h2>Expenses</h2>

//       <table border="1" cellPadding="8" cellSpacing="0">
//         <thead>
//           <tr>
//             <th>Title</th>
//             <th>Category</th>
//             <th>Amount</th>
//             <th>Date</th>
//             <th>Action</th>
//           </tr>
//         </thead>

//         <tbody>
//           {expenses.map((expense) => (
//             <tr key={expense.id}>
//               <td>{expense.title}</td>
//               <td>{expense.category}</td>
//               <td>{expense.amount}</td>
//               <td>{expense.date}</td>
//               <td>
//                 <button onClick={() => handleDelete(expense.id)}>
//                   Delete
//                 </button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default ExpenseList;

import { deleteExpense } from "../services/api";

function ExpenseList({ expenses, onExpenseDeleted }) {
  const handleDelete = async (id) => {
    await deleteExpense(id);
    onExpenseDeleted();
  };

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-dark text-white">
        Expense History
      </div>

      <div className="card-body p-0">
        <table className="table table-striped table-hover mb-0">
          <thead className="table-light">
            <tr>
              <th>Title</th>
              <th>Category</th>
              <th>Amount</th>
              <th>Date</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            {expenses.map((e) => (
              <tr key={e.id}>
                <td>{e.title}</td>
                <td>{e.category}</td>
                <td className="fw-bold">{e.amount}</td>
                <td>{e.date}</td>
                <td className="text-end">
                  <button
                    className="btn btn-sm btn-danger"
                    onClick={() => handleDelete(e.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}

            {expenses.length === 0 && (
              <tr>
                <td colSpan="5" className="text-center text-muted">
                  No expenses recorded
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ExpenseList;

