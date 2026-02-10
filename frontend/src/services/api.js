// const BASE_URL = "https://smart-expense-tracker-u5mh.onrender.com/api/expenses";
// // const BASE_URL = "http://127.0.0.1:5000/api/expenses";

// export async function fetchExpenses() {
//   const response = await fetch(BASE_URL);
//   return response.json();
// }

// export async function addExpense(expense) {
//   const response = await fetch(BASE_URL, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(expense),
//   });

//   return response.json();
// }
// export async function fetchInsights() {
//   const response = await fetch("http://127.0.0.1:5000/api/expenses/insights");
//   return response.json();
// }
// export async function deleteExpense(id) {
//   const response = await fetch(
//     `http://127.0.0.1:5000/api/expenses/${id}`,
//     {
//       method: "DELETE",
//     }
//   );

//   return response.json();
// }
const BASE_URL = "https://smart-expense-tracker-u5mh.onrender.com/api/expenses";

export async function fetchExpenses() {
  const response = await fetch(BASE_URL);
  if (!response.ok) throw new Error("Failed to fetch expenses");
  return response.json();
}

export async function addExpense(expense) {
  const response = await fetch(BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(expense),
  });

  if (!response.ok) throw new Error("Failed to add expense");
  return response.json();
}

// export async function fetchInsights() {
//   const response = await fetch(`${BASE_URL}/insights`);
//   if (!response.ok) throw new Error("Failed to fetch insights");
//   return response.json();
// }

export async function fetchInsights() {
  const response = await fetch(
    "https://smart-expense-tracker-u5mh.onrender.com/api/ml-insights"
  );

  if (!response.ok) throw new Error("Failed to fetch insights");
  return response.json();
}


export async function deleteExpense(id) {
  const response = await fetch(`${BASE_URL}/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) throw new Error("Failed to delete expense");
  return response.json();
}
