import streamlit as st
import joblib
import pandas as pd
import os
from src.model_train import train_model

st.set_page_config(page_title="HR Predictor", layout="centered")

st.title("🧑‍💼 Employee Attrition Predictor")
st.write("Will this employee leave the company? (AI Prediction)")

# Check if model exists, if not train it
if not os.path.exists('model.pkl'):
    with st.spinner("Training Model for the first time..."):
        train_model()
    st.success("Model trained successfully!")

# Load Model
model = joblib.load('model.pkl')

# --- SIDEBAR INPUTS ---
st.sidebar.header("Employee Details")
age = st.sidebar.slider("Age", 18, 60, 30)
salary = st.sidebar.number_input("Monthly Income ($)", 1000, 20000, 5000)
overtime = st.sidebar.selectbox("Does Overtime?", ["No", "Yes"])
satisfaction = st.sidebar.slider("Job Satisfaction (1-4)", 1, 4, 3)
years = st.sidebar.slider("Years at Company", 0, 40, 5)
distance = st.sidebar.slider("Distance From Home (km)", 1, 50, 10)

# Hidden defaults (for simplicity)
daily_rate = 800
education = 3 

# Preprocess Input
overtime_val = 1 if overtime == "Yes" else 0
input_data = pd.DataFrame([[age, daily_rate, distance, education, satisfaction, years, salary, overtime_val]], 
                          columns=['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'JobSatisfaction', 'YearsAtCompany', 'MonthlyIncome', 'OverTime'])

# --- PREDICTION ---
if st.button("Predict Attrition Risk"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ High Risk! This employee is likely to leave. (Confidence: {prob:.1%})")
        st.markdown("**Suggested Action:** Schedule a retention meeting immediately.")
    else:
        st.success(f"✅ Safe. This employee is likely to stay. (Risk: {prob:.1%})")
