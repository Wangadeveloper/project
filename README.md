# Loan App – Pesapal Junior Dev Challenge 2026 Submission


## Overview

This project is my submission for the **Pesapal Junior Dev Challenge 2026**. It demonstrates **core database management principles**, a **custom relational database engine**, and a **fully functional web application** built with **Flask**.  

The application allows users to:

- **Register**, **login**, and **logout** securely  
- **Create and update user profiles**  
- **Apply for loans** and receive **personalized financial advice**  
- **Download professional PDF reports** generated from AI recommendations  

This project showcases both **backend engineering skills** (custom RDBMS + SQL concepts) and **frontend integration** (Flask web interface).

---

## Core Features

### 1. Custom RDBMS Engine

I implemented a **lightweight relational database engine** in Python that supports:

- **Table creation**: `CREATE TABLE users (...), CREATE TABLE profiles (...)`  
- **Insertion**: `INSERT INTO users VALUES (...)` and `INSERT INTO profiles VALUES (...)`  
- **Selection / querying**: `SELECT * FROM users WHERE email = ?`  
- **Updates**: `UPDATE profiles SET ... WHERE user_id = ?`  
- **Primary & unique keys**: Auto-incrementing IDs, unique emails, and username constraints  

✅ **Key SQL Concepts Demonstrated**:

| Concept                 | Implementation in App                                   |
|-------------------------|---------------------------------------------------------|
| CRUD Operations          | `INSERT`, `SELECT`, `UPDATE` through Python engine    |
| Table Joins              | Profiles linked to Users via `user_id`               |
| Primary & Unique Keys    | Enforced in memory, preventing duplicate users         |
| Data Persistence         | Tables stored as JSON (`users.json`, `profiles.json`) |
| Querying & Filtering     | WHERE clauses supported for email, ID, and user_id     |

---

### 2. Flask Web Application

The **Flask frontend** interacts with the custom RDBMS for all operations:

- **Authentication**:
  - Register: users provide `username`, `email`, and `password`  
  - Login / Logout: secure session management via **Flask-Login**  
- **Profile Management**:
  - Users can **create** and **update** their profile  
  - All profile fields are validated using **WTForms** and **validators**  
- **Loan Application & AI Advice**:
  - Users enter their **business type, income, and repayment details**  
  - App sends this data to a **Gemini AI model** for personalized financial advice  
  - AI recommendations are compiled into **downloadable PDF reports** ,the download link appears at the bottom of the same form after submission and analysis is made

---

### 3. Gemini AI Integration – Cherry on the Cake

The project incorporates **Google’s Gemini AI** for advanced financial analysis:

- **Prompt-based financial advice generation**  
- Generates clear and actionable **loan recommendations**  
- Outputs professional **PDF reports** using **FPDF**  
- Fully integrated with the Flask app – **users can download PDFs** directly  

---

### 4. User Flow

1. **Register / Login**  
2. **Update Profile**  
3. **Access Dashboard**  
4. **Submit Loan Risk Assessment Form**  
5. **Download AI-generated PDF report**  

All user data is securely stored in the **custom RDBMS**.

---

![try out the website](https://project-9fwd.onrender.com/)

## Directory Structure

```bash
loan-app/
│
├── run.py                     # Flask app entry point
├── loan/
│   ├── __init__.py            # Flask app factory
│   ├── routes.py              # App routes for register, login, profile, dashboard
│   ├── forms.py               # WTForms definitions
│   ├── auth.py                # Login helpers for Flask-Login
│   ├── repositories/          # DB access layer
│   │   ├── user_repo.py
│   │   └── profile_repo.py
│   ├── rdbms/                 # Custom RDBMS engine
│   │   ├── database.py
│   │   ├── executor.py
│   │   └── bootstrap.py
│   ├── gemini_engine.py       # AI integration + PDF generation
│   ├── static/
│   │   └── reports/           # Generated PDFs
│   └── templates/             # HTML templates
└── requirements.txt
