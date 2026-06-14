# placement-predictor
# 🎓 Placement Prediction System

## Overview

A Machine Learning web application that predicts whether a student is likely to be placed based on their CGPA and IQ score.

The project uses Logistic Regression for classification, StandardScaler for feature preprocessing, and Streamlit for deployment as an interactive web application.

---

## Features

* Predicts placement outcome (Placed / Not Placed)
* Uses CGPA and IQ as input features
* Real-time prediction through a web interface
* Displays placement probability
* Deployed using Streamlit Cloud

---

## Tech Stack

* Python
* Streamlit
* Scikit-Learn
* NumPy
* Pandas

---

## Machine Learning Workflow

1. Data Preprocessing
2. Feature Scaling using StandardScaler
3. Model Training using Logistic Regression
4. Model Serialization using Pickle
5. Deployment using Streamlit

---

## Project Structure

placement-predictor/

├── app.py

├── model.pkl

├── scaler.pkl

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository:

git clone https://github.com/ayushsankhyan/placement-predictor.git

Move into the project directory:

cd placement-predictor

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Future Improvements

* Better UI/UX design
* Additional student performance features
* Multiple ML model comparison
* Visualization dashboard
* Placement analytics

---

## Author

Ayush Sankhyan

Computer Science Engineering
with specialization in AIML
