import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Climate Risk Twin", layout="wide")

st.title("🌍 Climate Risk Digital Twin Platform")

st.markdown("Simulate climate risk and financial impact across company assets.")

# Load model
model = joblib.load("risk_model.pkl")

# Sidebar
st.sidebar.header("Controls")
year = st.sidebar.slider("Select Year", 2000, 2035, 2025)

# Prediction
prediction = model.predict([[year]])

st.subheader("📈 Predicted Climate Risk")
st.metric(label="Risk Score", value=f"{prediction[0]:.2f}")

# Load data
df = pd.read_csv("final_results.csv")

# Show data
st.subheader("🏭 Asset Overview")
st.dataframe(df)

# Highlight risk
high_risk = df[df["asset_risk"] > 0.6]

st.subheader("⚠️ High Risk Assets")
st.write(high_risk)
