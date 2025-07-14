{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d4c05835-0a2c-4ee1-a949-33b27f07d3f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-09 10:30:01.088 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\user\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-07-09 10:30:01.093 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load trained model\n",
    "model = joblib.load(\"Diabetes.joblib\")\n",
    "\n",
    "st.title(\"Diabetes Prediction App\")\n",
    "\n",
    "# User input form\n",
    "Gender = st.selectbox(\"Gender\", [\"Male\", \"Female\", \"Other\"])\n",
    "Age = st.slider(\"Age\", 1, 100)\n",
    "Hypertension = st.selectbox(\"Hypertension\", [0, 1])\n",
    "Heart_disease = st.selectbox(\"Heart Disease\", [0, 1])\n",
    "Smoking_history = st.selectbox(\"Smoking History\", [\"never\", \"former\", \"current\", \"No Info\", \"ever\", \"not current\"])\n",
    "Bmi = st.number_input(\"BMI\", min_value=10.0)\n",
    "Hba1c_level = st.number_input(\"HbA1c Level\", min_value=3.0)\n",
    "Glucose = st.number_input(\"Blood Glucose Level\", min_value=30.0)\n",
    "\n",
    "# Create DataFrame\n",
    "input_data = pd.DataFrame([{\n",
    "    \"gender\": Gender,\n",
    "    \"age\": Age,\n",
    "    \"hypertension\": Hypertension,\n",
    "    \"heart_disease\": Heart_disease,\n",
    "    \"smoking_history\": Smoking_history,\n",
    "    \"bmi\": Bmi,\n",
    "    \"HbA1c_level\": Hba1c_level,\n",
    "    \"blood_glucose_level\": Glucose\n",
    "}])\n",
    "\n",
    "# Encode categorical variables AFTER creating input_data\n",
    "input_data[\"gender\"] = input_data[\"gender\"].map({\"Male\": 1, \"Female\": 0, \"Other\": 2})\n",
    "input_data[\"smoking_history\"] = input_data[\"smoking_history\"].map({\n",
    "    \"never\": 0, \"former\": 1, \"current\": 2, \"No Info\": 3, \"ever\": 4, \"not current\": 5\n",
    "})\n",
    "\n",
    "# Make prediction\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\"Prediction: {'🔴 High Diabetes Risk' if prediction[0] == 1 else '🟢 Likely Non-Diabetic'}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f0c3f52-d1b6-4d32-9727-a9bf0a591327",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
