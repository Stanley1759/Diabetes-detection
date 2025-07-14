import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("Diabetes.joblib")

st.title("🩺 Diabetes Prediction App")

# User input form
Gender = st.selectbox("Gender", ["Male", "Female", "Other"])
Age = st.slider("Age", 1, 100)
Hypertension = st.selectbox("Hypertension", [0, 1])
Heart_disease = st.selectbox("Heart Disease", [0, 1])
Smoking_history = st.selectbox("Smoking History", ["never", "former", "current", "No Info", "ever", "not current"])
Bmi = st.number_input("BMI", min_value=10.0)
Hba1c_level = st.number_input("HbA1c Level", min_value=3.0)
Glucose = st.number_input("Blood Glucose Level", min_value=30.0)

# Create DataFrame
input_data = pd.DataFrame([{
    "gender": Gender,
    "age": Age,
    "hypertension": Hypertension,
    "heart_disease": Heart_disease,
    "smoking_history": Smoking_history,
    "bmi": Bmi,
    "HbA1c_level": Hba1c_level,
    "blood_glucose_level": Glucose
}])

# Encode categorical variables AFTER creating input_data
input_data["gender"] = input_data["gender"].map({"Male": 1, "Female": 0, "Other": 2})
input_data["smoking_history"] = input_data["smoking_history"].map({"never": 0, "former": 1, "current": 2, "No Info": 3, "ever": 4, "not current": 5
})

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'🔴 High Diabetes Risk' if prediction[0] == 1 else '🟢 Likely Non-Diabetic'}")
