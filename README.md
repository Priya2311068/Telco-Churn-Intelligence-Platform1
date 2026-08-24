# 📊 Telco Customer Churn Intelligence Platform

An end-to-end customer churn analytics and prediction platform built using Power BI, Python, Machine Learning, and Streamlit.

## 🚀 Live Application

👉 **[Open Live Streamlit Application](https://telco-churn-intelligence-priya.streamlit.app/)**

## 🛠️ Technologies Used

- Power BI
- Python
- Pandas
- Scikit-learn
- Logistic Regression
- Streamlit
- SQL
- Data Visualization
- Machine Learning
## 🚀 Project Overview

Customer churn is a major challenge for telecom companies because losing existing customers directly impacts recurring revenue and customer lifetime value.

This project goes beyond simply predicting whether a customer may churn.

It provides an integrated decision-support system that helps answer:

- Which customers are most likely to churn?
- What factors are driving customer churn?
- Which customer segments have the highest churn rates?
- How much revenue is potentially at risk?
- Which customers should be prioritized for retention?
- What retention actions can be recommended?
- How does customer lifetime value vary across segments?

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Analyze customer churn patterns and business drivers
- Build a machine-learning model for churn prediction
- Estimate individual customer churn probability
- Segment customers into different risk levels
- Identify high-risk customers
- Analyze revenue and customer lifetime value
- Provide actionable retention recommendations
- Build an interactive Streamlit application for business users

---

# 🏗️ Application Structure

The Streamlit application is organized into four major analytical modules:

### 🔮 1. Churn Prediction

Provides customer-level churn prediction using the trained machine-learning model.

Key functionality:

- Customer information input
- Churn probability estimation
- Churn / No-Churn prediction
- Risk-level classification
- Decision threshold-based prediction
- Customer-specific retention guidance

---

### 📊 2. Business Analytics

Provides an executive view of customer churn and its major business drivers.

Key metrics include:

- Total Customers
- Churned Customers
- Churn Rate
- Monthly Revenue Lost
- Total Revenue Lost
- Average Customer Tenure

Key analyses include:

- Churn Rate by Internet Service
- Churn Risk vs Customer Tenure
- Churn Rate by Contract
- Churn by Tenure Cohort
- Top Churn Reasons
- Churn by Online Security
- Average Monthly Charges
- Recommended Retention Actions

Interactive filters allow users to explore churn across different customer segments.

---

### 💰 3. Customer Segment & Revenue Analysis

Focuses on customer value, segmentation, revenue behavior, and retention opportunities.

Key metrics include:

- Total Revenue
- Average Total Charges
- Average Monthly Charges
- Average Customer Lifetime Value (CLTV)

Key analyses include:

- Average Revenue by Churn Status
- Churn Rate by Dependents
- Churn Rate by Senior Citizen
- Churn Rate by Payment Method
- Average CLTV by Tenure Group
- Contract × Payment Method Churn Analysis
- Customer Segment Insights
- Business Recommendations

This module helps connect **customer churn with financial impact and long-term customer value**.

---

### 🚨 4. High Risk Customer Retention Center

A dedicated decision-support page for identifying and prioritizing customers requiring retention attention.

Key metrics include:

- Number of High-Risk Customers
- Average Churn Probability
- Revenue at Risk
- Average CLTV at Risk

Key analyses include:

- Highest Churn Probability Customers
- Revenue at Risk by Contract
- Recommended Retention Actions
- Customer Risk Distribution

The **High Risk Customer Watchlist** provides customer-level information including:

- Customer ID
- Risk Level
- Churn Probability
- Contract
- Internet Service
- Payment Method
- Monthly Charges
- Tenure
- CLTV
- Online Security
- Recommended Action

This allows business teams to move from **analysis → prioritization → retention action**.

---

# 🤖 Machine Learning Model

The churn prediction system uses a:

**Logistic Regression Classifier**

The model was selected for its balance between predictive performance and interpretability.

### Model Pipeline

The ML workflow includes:

1. Data preprocessing
2. Missing-value handling
3. Categorical feature encoding
4. Numerical feature preparation
5. Train-test splitting
6. Logistic Regression training
7. Probability prediction
8. Decision-threshold optimization
9. Risk segmentation
10. Customer-level retention recommendations

### Decision Threshold

The application uses a custom decision threshold of:

```text
0.62
```

Instead of relying only on the default 0.50 threshold, threshold tuning was used to better balance churn detection and prediction quality.

---

# 📈 Model Performance

The trained model achieved approximately:

| Metric | Performance |
|---|---:|
| Accuracy | 74.52% |
| Precision | 51.31% |
| Recall | 78.34% |
| F1 Score | 62.01% |
| ROC-AUC | 84.80% |

The relatively strong recall helps the system identify a larger proportion of customers who are actually at risk of churn.

---

# 🔍 Key Business Insights

The analysis revealed several important churn patterns:

- **Month-to-month customers show substantially higher churn risk** than customers with longer contracts.
- **Fiber optic customers** represent an important churn-risk segment.
- Customers using **electronic check** show particularly high churn behavior.
- Customers without **Online Security** and **Tech Support** show elevated churn tendencies.
- Customer churn generally declines as **tenure increases**.
- Long-tenure customers generate stronger customer lifetime value.
- High-value customers with elevated churn probability should receive greater retention priority.

---

# 💡 Retention Strategy

The platform converts analytical findings into practical business actions.

### RETAIN
Prioritize vulnerable and high-value customers with targeted retention offers.

### PROTECT
Promote Online Security and address service-related problems among high-risk customers.

### ENGAGE
Focus proactive retention campaigns on customers during their early tenure period.

### CONVERT
Encourage high-risk month-to-month customers to move toward one-year or two-year contracts.

### GROW
Use loyalty rewards and tenure-based benefits to improve long-term customer lifetime value.

---

# 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and analytics |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning |
| Logistic Regression | Churn prediction |
| Streamlit | Interactive web application |
| Plotly | Interactive visualizations |
| Power BI | Business intelligence and dashboarding |
| Joblib | Saving/loading ML artifacts |
| Git & GitHub | Version control and project hosting |

---

# 📁 Suggested Project Structure

```text
Telco-Churn-Intelligence-Platform/
│
├── app.py
│
├── pages/
│   ├── 2_🔮_Churn_Prediction.py
│   ├── 3_📊_Business_Analytics.py
│   ├── 4_💰_Customer_Segment_Revenue.py
│   └── 5_🚨_High_Risk_Customers.py
│
├── data/
│   └── telco_customer_churn.csv
│
├── models/
│   ├── churn_model.pkl
│   └── preprocessor.pkl
│
├── assets/
│   └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder and file names may vary depending on the final project structure.

---

# ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Move into the project directory

```bash
cd Telco-Churn-Intelligence-Platform
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will then open in your browser.

---

# 📦 requirements.txt

Typical dependencies for this project include:

```text
streamlit
pandas
numpy
scikit-learn
plotly
joblib
```

Make sure the versions used during deployment are compatible with the versions used to train and save the machine-learning model.

---

# 🖥️ Application Workflow

```text
                  TELCO CUSTOMER DATA
                          │
                          ▼
                 Data Preprocessing
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       Business Analytics      Machine Learning
              │                       │
              ▼                       ▼
       Churn Insights          Churn Probability
              │                       │
              └───────────┬───────────┘
                          ▼
                  Risk Segmentation
                          │
                          ▼
                 High-Risk Customers
                          │
                          ▼
                Revenue / CLTV Impact
                          │
                          ▼
              Retention Recommendations
```

---

# 🌟 Key Features

- 📊 Interactive churn analytics
- 🔮 Machine-learning churn prediction
- 🎯 Customer-level churn probability
- 🚦 Customer risk segmentation
- 🚨 High-risk customer identification
- 💰 Revenue-at-risk analysis
- 💎 Customer lifetime value analysis
- 📋 High-risk customer watchlist
- 💡 Automated retention recommendations
- 🎛️ Interactive business filters
- 📈 Executive-level KPIs
- 🌐 Streamlit-based web interface

---

# 💼 Business Value

This project demonstrates how data analytics and machine learning can be integrated into a single business application.

Instead of stopping at:

> **“Which customers will churn?”**

the platform extends the analysis to:

> **“Who is at risk, why are they at risk, how much value is exposed, and what should the business do about it?”**

This makes the project useful as both a **data analytics solution** and a **customer-retention decision-support system**.

---

# 🔮 Future Improvements

Potential improvements include:

- XGBoost / Random Forest model comparison
- SHAP-based prediction explanations
- Customer-level feature importance
- Real-time prediction API
- Automated retention campaign recommendations
- Database integration
- Model monitoring
- Automated model retraining
- Cloud deployment
- Authentication for business users
- Downloadable high-risk customer reports

---

# 👩‍💻 Author

**Priya Jangra**

B.Tech – Artificial Intelligence & Machine Learning  
Aspiring Data Analyst | Power BI Developer | Python & SQL Enthusiast

### Core Skills

`Python` • `SQL` • `Power BI` • `Excel` • `Pandas` • `NumPy` • `Machine Learning` • `Streamlit` • `Data Visualization`

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a **⭐ Star**.

---

### 📌 Project Status

**Active / Portfolio Project**

The platform currently integrates:

**Business Analytics + Machine Learning + Customer Segmentation + Revenue Analysis + Risk Prioritization + Retention Intelligence**
