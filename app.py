import streamlit as st

st.set_page_config(
    page_title="Telco Churn Analytics",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Telco Customer Churn Analytics")

st.markdown("""
## Customer Retention & Churn Intelligence

This application combines:

- 📊 Business analytics
- 🤖 Machine learning churn prediction
- 🎯 High-risk customer identification
- 💡 Retention recommendations

Use the navigation menu on the left to explore the application.
""")

st.divider()

st.subheader("🚀 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Business Analytics", "Power BI")

with col2:
    st.metric("ML Model", "Logistic Regression")

with col3:
    st.metric("Decision Threshold", "0.62")

st.divider()

st.info(
    "Use the sidebar to open the Churn Prediction module."
)