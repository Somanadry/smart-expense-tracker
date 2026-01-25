// import { useState } from "react";
// import { addExpense } from "../services/api";

// function ExpenseForm({ onExpenseAdded }) {
//   const [title, setTitle] = useState("");
//   const [amount, setAmount] = useState("");
//   const [category, setCategory] = useState("");
//   const [date, setDate] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     const expense = {
//       title,
//       amount: parseFloat(amount),
//       category,
//       date,
//     };

//     await addExpense(expense);

//     setTitle("");
//     setAmount("");
//     setCategory("");
//     setDate("");

//     onExpenseAdded();
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <h2>Add Expense</h2>

//       <input
//         type="text"
//         placeholder="Title"
//         value={title}
//         onChange={(e) => setTitle(e.target.value)}
//         required
//       />

//       <input
//         type="number"
//         placeholder="Amount"
//         value={amount}
//         onChange={(e) => setAmount(e.target.value)}
//         required
//       />

//       <input
//         type="text"
//         placeholder="Category"
//         value={category}
//         onChange={(e) => setCategory(e.target.value)}
//         required
//       />

//       <input
//         type="date"
//         value={date}
//         onChange={(e) => setDate(e.target.value)}
//         required
//       />

//       <button type="submit">Add</button>
//     </form>
//   );
// }

// export default ExpenseForm;
import { useState } from "react";
import { addExpense } from "../services/api";

function ExpenseForm({ onExpenseAdded }) {
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [date, setDate] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    await addExpense({
      title,
      amount: parseFloat(amount),
      category,
      date,
    });

    setTitle("");
    setAmount("");
    setCategory("");
    setDate("");

    onExpenseAdded();
  };

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-primary text-white">
        Add Expense
      </div>

      <div className="card-body">
        <form onSubmit={handleSubmit}>
          <input
            className="form-control mb-3"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />

          <input
            className="form-control mb-3"
            type="number"
            placeholder="Amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />

          <input
            className="form-control mb-3"
            placeholder="Category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          />

          <input
            className="form-control mb-3"
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />

          <button className="btn btn-success w-100">
            Add Expense
          </button>
        </form>
      </div>
    </div>
  );
}

export default ExpenseForm;
