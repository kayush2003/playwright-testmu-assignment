# Playwright TestMu Assignment

## 📌 Overview

This project is an end-to-end UI automation test suite built using **Playwright (Python)** and **Pytest** for the TestMu AI Selenium Playground.

It covers multiple user interaction scenarios including:

- Simple Form validation
- Drag & Drop Slider validation
- Input Form submission with validations
- Parallel cross-browser execution (Chromium & Firefox)

---

## 🛠 Tech Stack

- Python 3.x
- Playwright
- Pytest
- Pytest-Playwright
- Pytest-xdist (Parallel Execution)

---

## 📂 Project Structure
playwright-testmu/
│
├── tests/
│ ├── test_scenario1.py
│ ├── test_scenario2.py
│ ├── test_scenario3.py
│
├── pytest.ini
├── playwright.config.py
├── requirements.txt
├── .gitignore
└── README.md

---

## ✅ Test Scenarios Covered

### 🔹 Scenario 1 – Simple Form Demo
- Navigate to Selenium Playground
- Click “Simple Form Demo”
- Validate URL
- Enter message
- Verify displayed output

### 🔹 Scenario 2 – Drag & Drop Sliders
- Navigate to Drag & Drop Sliders
- Change slider value from 15 to 95
- Validate updated range value

### 🔹 Scenario 3 – Input Form Submit
- Navigate to Input Form Submit
- Validate required fields
- Fill all fields
- Select country from dropdown
- Submit form
- Validate success message

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/kayush2003/playwright-testmu-assignment.git

cd playwright-testmu-assignment

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Install Playwright Browsers
playwright install

---

## ▶️ Run Tests

### Run in Headed Mode
python -m pytest --browser chromium --headed

### Run in Parallel (Chromium + Firefox)
python -m pytest --browser chromium --browser firefox -n 2

---

## 📊 Features Implemented

- Cross-browser testing
- Parallel execution
- Robust locator strategy
- Strict mode handling
- Scoped locators for unstable DOM
- Clean Git structure
- Professional project organization

---

## 🧠 Key Automation Practices Used

- Scoped locators to avoid duplicate ID conflicts
- Avoided strict mode violations
- Used semantic and role-based selectors
- Avoided relying on hidden or duplicate DOM elements
- Structured tests for maintainability

---

## 📎 Author

Ayush Kumar  
Associate Engineer - TCL PVT. LTD.
Full Stack Developer | Automation Enthusiast

---

## 📌 Notes

This project was developed as part of the TestMu AI Automation Certification Assignment.

All tests are designed to run successfully across supported browsers with stable locator strategies.
