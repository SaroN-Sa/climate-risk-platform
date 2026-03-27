import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Climate Risk Twin", layout="wide")

st.title("🌍 Climate Risk Digital Twin Platform")

# Load model
model = joblib.load("risk_model.pkl")

# Sidebar
st.sidebar.header("Controls")
year = st.sidebar.slider("Select Year", 2000, 2035, 2025)

# Prediction
prediction = model.predict([[year]])
st.subheader("📈 Predicted Climate Risk")
st.metric("Risk Score", f"{prediction[0]:.2f}")

# Load data
df = pd.read_csv("final_results.csv")

st.subheader("🏭 Asset Overview")
st.dataframe(df)

# 🌍 MAP SECTION
st.subheader("🌍 Asset Risk Map")

# Create map centered on assets
m = folium.Map(location=[df["lat"].mean(), df["lon"].mean()], zoom_start=5)

# Add points
for _, row in df.iterrows():
    color = "green"
    if row["asset_risk"] > 0.7:
        color = "red"
    elif row["asset_risk"] > 0.4:
        color = "orange"

    popup = f"""
    <b>{row['name']}</b><br>
    Risk: {row['asset_risk']:.2f}<br>
    Loss: ${row['loss']}
    """

    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=10,
        color=color,
        fill=True,
        popup=popup
    ).add_to(m)

# Display map in Streamlit
st_folium(m, width=700, height=500)
