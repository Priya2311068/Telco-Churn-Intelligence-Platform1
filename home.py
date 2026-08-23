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
# LIGHT PROFESSIONAL THEME
# --------------------------------------------------

st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #F7F9FC;
    color: #172033;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #172033;
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Main title */
h1 {
    color: #172033 !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px;
}

/* Subheadings */
h2, h3 {
    color: #172033 !important;
}

/* Paragraph text */
p, li {
    color: #475569;
}

/* Divider */
hr {
    border-color: #E2E8F0 !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #64748B;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #172033;
    font-weight: 700;
}

/* Module cards */
.module-card {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
    min-height: 175px;
}

/* Accent title */
.accent-title {
    color: #0EA5A8;
    font-weight: 700;
}

/* Hero badge */
.hero-badge {
    display: inline-block;
    background-color: #E6FFFB;
    color: #0F766E;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Intro box */
.intro-box {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 5px solid #0EA5A8;
    border-radius: 14px;
    padding: 22px 24px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

/* Footer */
.footer-text {
    color: #94A3B8;
    font-size: 0.85rem;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HOME PAGE HERO
# --------------------------------------------------

st.markdown(
    '<div class="hero-badge">Customer Analytics & Predictive Intelligence</div>',
    unsafe_allow_html=True
)

st.title("Telco Customer Churn Analytics")

st.markdown("""
<div class="intro-box">

<h3 style="margin-top:0;">Customer Retention & Churn Intelligence</h3>

<p>
A complete analytics solution combining business intelligence,
customer segmentation and machine-learning based churn prediction.
</p>

<p>
Explore customer behaviour, understand churn drivers, identify
high-risk customers and support targeted retention decisions.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------

st.subheader("Project Overview")

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

st.subheader("Application Modules")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="module-card">
        <h3 class="accent-title">Churn Prediction</h3>
        <p>
        Predict individual customer churn probability using the trained
        machine-learning model and assign a customer risk level.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3 class="accent-title">Customer Segment & Revenue</h3>
        <p>
        Analyze customer value, revenue patterns, payment behaviour,
        tenure groups and customer segments.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="module-card">
        <h3 class="accent-title">Business Analytics</h3>
        <p>
        Explore churn KPIs, customer behaviour, service patterns
        and the major business drivers associated with churn.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3 class="accent-title">High-Risk Customers</h3>
        <p>
        Identify customers requiring immediate retention attention
        and review recommended retention actions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# BUSINESS VALUE
# --------------------------------------------------

st.divider()

st.subheader("Business Objective")

st.markdown("""
The platform is designed to help a telecom business move from
**descriptive analytics to proactive retention**:

**Understand churn → Identify risk → Prioritize customers → Take action**
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer-text">
Telco Churn Intelligence Platform • Python • Streamlit •
Machine Learning • Power BI • Business Analytics
</div>
""", unsafe_allow_html=True)
