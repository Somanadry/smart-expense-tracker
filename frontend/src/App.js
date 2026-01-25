// // import { useEffect, useState } from "react";
// // import ExpenseForm from "./components/ExpenseForm";
// // import ExpenseList from "./components/ExpenseList";
// // import { fetchExpenses } from "./services/api";
// // import AIInsights from "./components/AIInsights";
// // import ExpenseSummary from "./components/ExpenseSummary";



// // function App() {
// //   const [expenses, setExpenses] = useState([]);

// //   const loadExpenses = async () => {
// //     const data = await fetchExpenses();
// //     setExpenses(data);
// //   };

// //   useEffect(() => {
// //     loadExpenses();
// //   }, []);

// //   return (
// //     <div>
// //       <h1>Smart Expense Tracker</h1>
// //       <ExpenseForm onExpenseAdded={loadExpenses} />
// //       <ExpenseList
// //        expenses={expenses}
// //        onExpenseDeleted={loadExpenses}
// //       />
// //       <ExpenseSummary expenses={expenses} />

// //       <AIInsights />

// //     </div>
// //   );
// // }

// // export default App;

// import { useEffect, useState } from "react";
// import ExpenseForm from "./components/ExpenseForm";
// import ExpenseList from "./components/ExpenseList";
// import ExpenseSummary from "./components/ExpenseSummary";
// import AIInsights from "./components/AIInsights";
// import { fetchExpenses } from "./services/api";
// // const [theme, setTheme] = useState("light");
//   const [theme, setTheme] = useState(
//   localStorage.getItem("theme") || "light"
// );

// function App() {
//   const [expenses, setExpenses] = useState([]);


// useEffect(() => {
//   document.body.setAttribute("data-bs-theme", theme);
//   localStorage.setItem("theme", theme);
// }, [theme]);

//   const loadExpenses = async () => {
//     const data = await fetchExpenses();
//     setExpenses(data);
//   };

//   useEffect(() => {
//     loadExpenses();
//   }, []);
// //   useEffect(() => {
// //   document.body.setAttribute("data-bs-theme", theme);
// // }, [theme]);


//   return (
//     // <div className="container-fluid container-md my-4 px-3">
//     //   {/* Header */}
//     //   <div className="mb-4 text-center">
//     //     <h1 className="fw-bold">Smart Expense Tracker</h1>
//     //     <p className="text-muted">
//     //       Track, analyze, and optimize your spending
//     //     </p>
//     //   </div>
// <div className="mb-4 d-flex justify-content-between align-items-center">
//   <div>
//     <h1 className="fw-bold">Smart Expense Tracker</h1>
//     <p className="text-muted mb-0">
//       Track, analyze, and optimize your spending
//        </p>
//          </div>

//        <button
//        className="btn btn-outline-secondary"
//         onClick={() =>
//           setTheme(theme === "light" ? "dark" : "light")
//        }
//        >
//           {theme === "light" ? "Dark Mode" : "Light Mode"}
//         </button>



//       {/* Form + Summary */}
//       <div className="row g-4 mb-4">
//         <div className="col-md-6">
//           <ExpenseForm onExpenseAdded={loadExpenses} />
//         </div>
//         <div className="col-md-6">
//           <ExpenseSummary expenses={expenses} />
//         </div>
//       </div>

//       {/* Expense List */}
//       <div className="mb-4">
//         <ExpenseList
//           expenses={expenses}
//           onExpenseDeleted={loadExpenses}
//         />
//       </div>

//       {/* AI Insights */}
//       <div className="mt-4">
//         <AIInsights />
//       </div>
//     </div>
//   );
// }

// export default App;


import { useEffect, useState } from "react";
import ExpenseForm from "./components/ExpenseForm";
import ExpenseList from "./components/ExpenseList";
import ExpenseSummary from "./components/ExpenseSummary";
import AIInsights from "./components/AIInsights";
import { fetchExpenses } from "./services/api";

function App() {
  const [expenses, setExpenses] = useState([]);

  // const [theme, setTheme] = useState("light");
  const [theme, setTheme] = useState(
    localStorage.getItem("theme") || "light"
  );

  useEffect(() => {
    document.body.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  const loadExpenses = async () => {
    const data = await fetchExpenses();
    setExpenses(data);
  };

  useEffect(() => {
    loadExpenses();
  }, []);

  // useEffect(() => {
  //   document.body.setAttribute("data-bs-theme", theme);
  // }, [theme]);

  return (
    <div className="container-fluid container-md my-4 px-3">
      <div className="mb-4 d-flex justify-content-between align-items-center">
        <div>
          <h1 className="fw-bold">Smart Expense Tracker</h1>
          <p className="text-muted mb-0">
            Track, analyze, and optimize your spending
          </p>
        </div>

        <button
          className="btn btn-outline-secondary"
          onClick={() =>
            setTheme(theme === "light" ? "dark" : "light")
          }
        >
          {theme === "light" ? "Dark Mode" : "Light Mode"}
        </button>
      </div>

      {/* Form + Summary */}
      <div className="row g-4 mb-4">
        <div className="col-md-6">
          <ExpenseForm onExpenseAdded={loadExpenses} />
        </div>
        <div className="col-md-6">
          <ExpenseSummary expenses={expenses} />
        </div>
      </div>

      {/* Expense List */}
      <div className="mb-4">
        <ExpenseList
          expenses={expenses}
          onExpenseDeleted={loadExpenses}
        />
      </div>

      {/* AI Insights */}
      <div className="mt-4">
        <AIInsights />
      </div>
    </div>
  );
}

export default App;
