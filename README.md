# Job Acceptance Prediction System

## 📌 Project Overview
The Job Acceptance Prediction System is a machine learning project designed to predict whether a candidate will **accept or reject a job offer** based on demographic details, academic performance, skills, experience, salary expectations, and job-related factors.

This system helps recruiters and HR teams make **data-driven hiring decisions** and reduce offer drop rates.

---

## 🎯 Problem Statement
Recruiters often face uncertainty after extending job offers, leading to:
- High offer rejection rates
- Increased hiring costs
- Wasted recruitment efforts

This project aims to build a predictive model that estimates job acceptance likelihood in advance.

---

## 🧠 Solution Approach
The project follows an end-to-end machine learning pipeline:
1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Building
6. Model Evaluation
7. Streamlit Web App Deployment

---

## 📊 Dataset Information
- Records: ~51,500
- Features: 26
- Target Variable: `status`
  - `Placed` → Accepted Job
  - `Not Placed` → Rejected Job
- Problem Type: Binary Classification

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Models
- Logistic Regression
- Decision Tree
- Random Forest (Final Model)

Random Forest was selected due to its superior performance and ability to handle non-linear relationships.

---

## 🌐 Web Application
A Streamlit-based web application allows recruiters to:
- Enter candidate details
- Predict job acceptance in real time

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Job-Acceptance-Prediction
2. Create & Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate
3. Install Requirements
pip install -r requirements.txt
4. Run Streamlit App
python -m streamlit run app.py
