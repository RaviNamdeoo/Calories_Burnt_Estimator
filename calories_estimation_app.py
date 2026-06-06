import streamlit as st
import pandas as pd
import numpy as np
import pickle

xgb = pickle.load(open('artifacts/XGBoost_model.pkl','rb'))

st.title("Calories Burnt Estimator App")

gender = st.selectbox('Gender',['Male','Female'])
age = st.number_input('Age', min_value=12, max_value=100, value=30)
height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, value=170.0, step=0.5)
weight = st.number_input('Weight (kg)', min_value=35.0, max_value=200.0, value=70.0, step=0.5)
duration = st.number_input('Exercise Duration (minutes)', min_value=1.0, max_value=300.0, value=15.0, step=1)
heart_rate = st.number_input('Heart Rate (bpm)', min_value=40.0, max_value=200.0, value=100.0, step=1)
body_temp = st.number_input('Body Temperature (°C)', min_value=36.0, max_value=43.0, value=39.0, step=0.1)

gender_encoded = 0 if gender == 'Male' else 1

if st.button('Predict Calories Burnt'):
    input_data = pd.DataFrame([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]],
                               columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
    
    prediction = xgb.predict(input_data)[0]
    
    st.success(f"Estimated Calories Burnt: **{prediction:.2f} kcal**")
