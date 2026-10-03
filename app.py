import streamlit as st
import joblib

# Load trained model
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="Height to Weight Predictor",
    page_icon="📏",
    layout="wide"
)

st.title("Height & Weight Prediction")
st.write("Enter a person's height to predict their weight.")

height = st.number_input(
    "Enter Height (cm)",
    min_value=137.83,
    max_value=200.66,
    value=150.0,
    step=0.1,
    help="Dataset range: approximately 137.83–200.66 cm"
)

if st.button("Predict Weight "):

    prediction = model.predict([[height]])

    st.success(
        f"Predicted Weight: {prediction[0]:.2f} kg"
    )
