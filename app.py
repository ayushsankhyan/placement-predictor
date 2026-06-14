import streamlit as st
import pickle
import numpy as np

# Page Config
st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load Model and Scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Title
st.title("🎓 Placement Prediction System")

st.markdown("""
Predict whether a student is likely to get placed based on:

- CGPA
- IQ Score

Built using Machine Learning and Logistic Regression.
""")

# Inputs
cgpa = st.slider(
    "Select CGPA",
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

iq = st.slider(
    "Select IQ",
    min_value=0,
    max_value=200,
    value=100
)

# Predict Button
if st.button("Predict Placement"):

    data = np.array([[cgpa, iq]])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)

    probability = model.predict_proba(scaled_data)

    confidence = probability[0][1] * 100

    st.divider()

    if prediction[0] == 1:
        st.success("✅ Student is likely to be Placed")
    else:
        st.error("❌ Student is likely NOT to be Placed")

    st.metric(
        label="Placement Probability",
        value=f"{confidence:.2f}%"
    )

    st.progress(float(confidence) / 100)

st.divider()

st.caption(
    "Built by Ayush Sankhyan."
)
