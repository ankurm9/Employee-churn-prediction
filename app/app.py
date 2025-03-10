import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("random_forest.pkl")

# App title and description
st.set_page_config(page_title="Employee Churn Prediction", layout="centered")
st.title("🔍 Employee Churn Prediction")
st.write("This app predicts whether an employee will leave the company based on various attributes.")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Select Page", ["Home", "Predict Employee Churn", "About"])

if page == "Home":
    st.subheader("Welcome to Employee Churn Predictor")
    st.write(
        "Use this tool to predict employee attrition based on their personal and professional attributes."
    )
    st.write("Navigate to the **Predict Employee Churn** tab to make a prediction.")

elif page == "Predict Employee Churn":
    st.subheader("Enter Employee Details")
    
    # Input fields for employee attributes
    age = st.number_input("Age", min_value=18, max_value=65, value=30, step=1)
    education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"], index=0)
    payment_tier = st.selectbox("Salary Tier", [1, 2, 3], index=1)
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    ever_benched = st.selectbox("Ever Benched?", ["Yes", "No"], index=1)
    experience = st.slider("Experience in Current Domain (Years)", min_value=0, max_value=40, value=5)
    
    # Encoding categorical variables
    education_map = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
    gender_map = {"Male": 0, "Female": 1}
    benched_map = {"Yes": 1, "No": 0}
    
    features = np.array([
        age,
        education_map[education],
        payment_tier,
        gender_map[gender],
        benched_map[ever_benched],
        experience
    ]).reshape(1, -1)
    
    # Predict button
    if st.button("Predict Churn"):
        prediction = model.predict(features)[0]
        result = "The employee is **likely to leave** the company." if prediction == 1 else "The employee is **likely to stay** in the company."
        st.success(result)

elif page == "About":
    st.subheader("About This App")
    st.write("This application is built using Streamlit and a trained Random Forest model to predict employee attrition.")
    st.write("Developed as part of the Employee Churn Prediction Project.")
