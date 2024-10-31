import streamlit as st
import joblib

model = joblib.load('Diabetes_Logistic.model')
st.title("Diabetes Prediction ")
col1,col2 = st.columns(2)

Pregnancies= col1.number_input(label="enter number of times impregnated", min_value=0, max_value=17)
Glucose = col2.number_input(label= "enter Glucose level", min_value=0, max_value=191)
BloodPressure = col1.number_input(label="enter Blood pressure level", min_value=0,max_value=114)
SkinThickness=col2.number_input(label="enter Skin thickness level", min_value=0,max_value=99)
Insulin=col1.number_input(label="Enter insulin level", min_value=0,max_value=846)
BMI=col2.number_input(label="Enter BMI Score", min_value=0,max_value=67)
DiabetesPredigreeFunction=col1.number_input(label="Enter DBF Score",min_value=0.078,max_value=2.42)
Age=col2.number_input(label="Enter Age",min_value=21,max_value=81)

if st.button("Predict"):
    prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPredigreeFunction,Age]])
    if prediction ==1:
        st.success("The model predict the patient would have Diabetes")
    else:
        st.warning("The model predict the patient does not have Diabetes")     