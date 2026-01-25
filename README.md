# Smart Expense Tracker

A full-stack web application to track personal expenses, analyze spending patterns, and generate AI-based spending insights.

This project was built as part of learning full-stack development and demonstrates real-world concepts like REST APIs, state management, CORS handling, and deployment readiness.

----------------------------------------------------
## 🌐 Live Demo

Frontend: https://smart-expense-tracker002.netlify.app/  
Backend API: https://smart-expense-tracker-u5mh.onrender.com/api/expenses


## 🚀 Tech Stack

### Frontend
- React (Functional Components, Hooks)
- Bootstrap 5 (Responsive UI, Dark Mode)
- Fetch API

### Backend
- Python Flask
- SQLite
- Flask-CORS

---

## ✨ Features

- Add expenses (title, amount, category, date)
- View all expenses in a table
- Delete expenses
- Category-wise expense summary
- Monthly spending analysis
- AI-generated spending insights (text-based)
- Responsive UI with Light/Dark mode toggle
- Persistent data storage using SQLite

---

## 📁 Project Structure

smart-expense-tracker/
├── backend/
│ ├── app/
│ │ ├── routes/
│ │ ├── services/
│ │ ├── extensions.py
│ │ └── config.py
│ ├── instance/
│ │ └── expenses.db
│ ├── run.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── services/
│ │ ├── App.js
│ │ └── index.js
│ ├── package.json
│ └── build/
│
└── README.md



---

## ▶️ How to Run Locally

### 1️⃣ Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python run.py
Backend Runs at: http://127.0.0.1:5000


FORNTEND--

cd frontend
npm install
npm start

frontend runs at :http://localhost:3000


🔌 API Endpoints
Method	Endpoint	Description
POST	/api/expenses	Add a new expense
GET	/api/expenses	Get all expenses
DELETE	/api/expenses/<id>	Delete an expense
GET	/api/expenses/categories	Category-wise totals
GET	/api/expenses/monthly?month=YYYY-MM	Monthly summary
GET	/api/expenses/insights	AI spending insights



🤖 AI Insights

The AI Insights feature analyzes expense data and returns a natural-language summary highlighting spending patterns and potential savings.

(Currently implemented using rule-based logic and designed to be extendable with real AI APIs.)



📌 Notes

Dark mode is toggle-based and persisted using localStorage

Designed with clean architecture and separation of concerns

Ready for deployment on platforms like Render (backend) and Netlify (frontend)


