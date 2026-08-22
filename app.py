import streamlit as st

st.set_page_config(
    page_title="Telco Churn Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

home = st.Page(
    "home.py",
    title="Home",
    icon="🏠",
    default=True
)

prediction = st.Page(
    "pages/2_🔮_Churn_Prediction.py",
    title="Churn Prediction",
    icon="🎯"
)

analytics = st.Page(
    "pages/3_📊_Business_Analytics.py",
    title="Business Analytics",
    icon="📊"
)

segment = st.Page(
    "pages/4_💰_Customer_Segment_Revenue.py",
    title="Customer Segment & Revenue",
    icon="💰"
)

risk = st.Page(
    "pages/5_🚨_High_Risk_Customers.py",
    title="High Risk Customers",
    icon="🚨"
)

pg = st.navigation(
    [
        home,
        prediction,
        analytics,
        segment,
        risk
    ],
    position="sidebar"
)

pg.run()
