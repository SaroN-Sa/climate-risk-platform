# 🌍 Climate Risk Digital Twin Platform

A data-driven platform that simulates how climate change impacts a company’s physical assets and supply chain.
It combines climate data, socio-economic indicators, and predictive modeling to estimate **risk, disruption, and financial loss**.

---

# 🚀 Project Overview

Companies often measure emissions, but few understand their **exposure to climate risk**.

This project builds a **Digital Twin** of a company's operations and applies **climate stress testing** to:

* Predict climate risk trends
* Simulate operational disruptions
* Estimate financial losses
* Provide actionable recommendations
* Visualize risk on a map

---

# 🧠 Key Concept (Simple Explanation)

Imagine:

👉 A company has factories, warehouses, and ports
👉 Climate change affects each location differently

This system:

1. Creates a **virtual version (digital twin)** of those assets
2. Uses climate + population + health data
3. Calculates risk for each location
4. Predicts future risk
5. Shows results in charts and maps

---

# ⚙️ Features

## 📈 1. Climate Risk Modeling

* Uses global temperature data
* Combines with population & life expectancy
* Generates a normalized risk score

---

## 🏭 2. Digital Twin (Assets Simulation)

* Models multiple company locations:

  * Factory
  * Warehouse
  * Port
* Each has:

  * Coordinates (lat/lon)
  * Revenue
  * Risk exposure

---

## 💰 3. Financial Impact Simulation

* Converts risk → shutdown days
* Calculates:

  * Operational disruptions
  * Financial losses

---

## 🔮 4. Future Risk Prediction

* Uses Linear Regression
* Predicts risk for next 5 years

---

## 🌍 5. Map Visualization

* Interactive map using Folium
* Color-coded risk:

  * 🔴 High
  * 🟠 Medium
  * 🟢 Low
* Clickable asset insights

---

## 📊 6. Dashboard

* Risk per asset
* Financial loss comparison
* Summary insights

---

## 🧠 7. AI Recommendations

* Suggests actions:

  * Relocate assets
  * Mitigate risks
  * Monitor conditions

---

## 🖥️ 8. Web Application

* Built with Streamlit
* Interactive interface
* Real-time prediction

---

# 🛠️ Technologies Used

## 🧑‍💻 Programming

* Python

## 📊 Data Handling

* pandas
* numpy

## 🤖 Machine Learning

* scikit-learn (Linear Regression)

## 🌍 Data Sources

* Global Temperature Dataset
* World Bank API (Population & Life Expectancy)

## 📈 Visualization

* matplotlib
* folium
* streamlit-folium

## 🌐 Web App

* Streamlit

## 💾 Model Storage

* joblib

## 📂 Version Control

* Git + GitHub

---

# 📂 Project Structure

```
climate-risk-platform/
│
├── app.py                 # Streamlit web app
├── risk_model.pkl         # Saved ML model
├── final_results.csv      # Processed asset data
├── requirements.txt       # Dependencies
│
├── notebooks/
│   └── climate_risk_demo.ipynb
│
└── README.md
```

---

# ▶️ How to Run Locally

## 1. Clone Repository

```
git clone https://github.com/SaroN-Sa/climate-risk-platform.git
cd climate-risk-platform
```

---

## 2. Install Requirements

```
pip install -r requirements.txt
```

---

## 3. Run App

```
streamlit run app.py
```

---

## 4. Open in Browser

```
http://localhost:8501
```

---

# 🌐 Deployment

This app is deployed using **Streamlit Cloud**.

👉 Live Demo: *(Add your link here)*

---

# 📊 Example Output

* Risk score prediction
* Asset risk comparison
* Financial loss estimation
* Interactive map visualization

---

# 🎯 Use Cases

* Manufacturing companies
* Logistics firms
* Ports and supply chains
* Insurance companies
* Climate risk analysts

---

# 🚧 Limitations

* Uses simplified datasets
* Limited number of assets
* Basic prediction model

---

# 🔮 Future Improvements

* Real-time satellite data integration
* Advanced ML models (LSTM, XGBoost)
* More climate indicators (flood, wind, drought)
* Multi-country comparison
* Interactive scenario simulation

---

# 🎤 Pitch Summary

> “We built a digital twin platform that simulates how climate change impacts physical assets. By combining climate data, socio-economic indicators, and AI, we predict risk, estimate financial losses, and provide actionable recommendations through an interactive web application.”

---

# 👨‍💻 Author

SaroN

---

# 📜 License

This project is for educational and competition purposes.
