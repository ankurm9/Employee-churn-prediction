import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/random_forest.pkl")

st.set_page_config(page_title="Employee Churn Prediction", layout="centered")
st.title("🔍 Employee Churn Prediction")

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

st.sidebar.title("📌 Navigate")
page = st.sidebar.radio(
    "",
    ["🏠 Home", "📊 Predict", "📈 Results", "ℹ️ About"],
    index=["🏠 Home", "📊 Predict", "📈 Results", "ℹ️ About"].index(st.session_state.page),
)

# Home Page
if page == "🏠 Home":
    st.session_state.page = "🏠 Home"
    st.subheader("Welcome to Employee Churn Predictor")
    st.write("Use this tool to predict employee attrition based on attributes.")
    st.write("Navigate to the **Predict** tab to make a prediction.")

# Prediction Page
elif page == "📊 Predict":
    st.session_state.page = "📊 Predict"
    st.subheader("Enter Employee Details")

    age = st.number_input("Age", min_value=18, max_value=65, value=30, step=1)
    education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"], index=0)
    payment_tier = st.selectbox("Salary Tier", [1, 2, 3], index=1)
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    ever_benched = st.selectbox("Ever Benched?", ["Yes", "No"], index=1)
    experience = st.slider("Experience in Current Domain (Years)", min_value=0, max_value=40, value=5)

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
    if st.button("🔍 Predict Churn"):
        prediction = model.predict(features)[0]
        st.session_state.prediction_result = (
            "✅ The employee is **likely to stay** in the company."
            if prediction == 0
            else "⚠️ The employee is **likely to leave** the company."
        )
        st.session_state.page = "📈 Results"
        st.experimental_rerun()  # Redirect to results page

# Results Page
elif page == "📈 Results":
    st.session_state.page = "📈 Results"
    st.subheader("📊 Prediction Results")
    
    if st.session_state.prediction_result:
        st.success(st.session_state.prediction_result)
    else:
        st.info("⚠️ No prediction made yet. Please go to **Predict Employee Churn** and enter details.")

# About Page
elif page == "ℹ️ About":
    st.session_state.page = "ℹ️ About"
    st.subheader("About This App")
    st.write("This application is built using Streamlit and a trained Random Forest model to predict employee attrition.")
    st.write("Developed as part of the Employee Churn Prediction Project.")
