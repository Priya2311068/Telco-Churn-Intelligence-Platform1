import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Telco Churn Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
st.title("📡 Telco Customer Churn Analytics")

st.markdown("""
## Customer Retention & Churn Intelligence

This application combines:

- 📊 **Business Analytics**
- 🔮 **Machine Learning Churn Prediction**
- 💰 **Customer Segmentation & Revenue Analysis**
- 🚨 **High-Risk Customer Identification**
- 💡 **Retention Recommendations**

Use the navigation menu on the left to explore the application.
""")

st.divider()

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------
st.subheader("🚀 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Business Analytics",
        value="Interactive"
    )

with col2:
    st.metric(
        label="ML Model",
        value="Logistic Regression"
    )

with col3:
    st.metric(
        label="Decision Threshold",
        value="0.62"
    )

st.divider()

# --------------------------------------------------
# APPLICATION MODULES
# --------------------------------------------------
st.subheader("🧭 Application Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🔮 Churn Prediction
    Predict individual customer churn probability using the trained
    machine-learning model.

    ### 💰 Customer Segment & Revenue
    Analyze customer value, revenue patterns, payment behaviour,
    tenure groups and customer segments.
    """)

with col2:
    st.markdown("""
    ### 📊 Business Analytics
    Explore churn KPIs, customer behaviour, churn drivers and
    important business insights.

    ### 🚨 High Risk Customers
    Identify customers requiring immediate retention attention and
    review recommended retention actions.
    """)

st.divider()

st.caption(
    "Telco Churn Intelligence Platform | Python • Streamlit • "
    "Machine Learning • Business Analytics"
)
