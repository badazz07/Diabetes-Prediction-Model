import streamlit as st
import joblib


model = joblib.load('Diabetes_Logistic.model')


st.set_page_config(page_title="Diabetes Prediction App", page_icon="")
st.markdown("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)


st.title("Diabetes Prediction ")
st.markdown("<hr>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input(label="Enter number of times pregnant", min_value=0, max_value=17, key="1")
    BloodPressure = st.number_input(label="Enter Blood pressure level", min_value=0, max_value=114, key="3")
    Insulin = st.number_input(label="Enter insulin level", min_value=0, max_value=846, key="5")
    DiabetesPredigreeFunction = st.number_input(label="Enter DBF Score", min_value=0.078, max_value=2.42, key="7")
    

with col2:
    Glucose = st.number_input(label="Enter Glucose level", min_value=0, max_value=191, key="2")
    SkinThickness = st.number_input(label="Enter Skin thickness level", min_value=0, max_value=99, key="4")
    BMI = st.number_input(label="Enter BMI Score", min_value=0, max_value=67, key="6")
    Age = st.number_input(label="Enter Age", min_value=21, max_value=81, key="9")


if st.button("Predict", type="primary"):
    prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])
    
    if prediction == 1:
        st.success("The model predicts the patient **will have** Diabetes")
    else:
        st.warning("The model predicts the patient **will not have** Diabetes")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>Developed by Abiodun Olawale </center>", unsafe_allow_html=True)