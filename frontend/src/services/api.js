const BASE_URL = "http://127.0.0.1:5000/api/expenses";

export async function fetchExpenses() {
  const response = await fetch(BASE_URL);
  return response.json();
}

export async function addExpense(expense) {
  const response = await fetch(BASE_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(expense),
  });

  return response.json();
}
export async function fetchInsights() {
  const response = await fetch("http://127.0.0.1:5000/api/expenses/insights");
  return response.json();
}
export async function deleteExpense(id) {
  const response = await fetch(
    `http://127.0.0.1:5000/api/expenses/${id}`,
    {
      method: "DELETE",
    }
  );

  return response.json();
}
