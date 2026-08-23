import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Telco Churn Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PROFESSIONAL LIGHT THEME
# ==========================================================

st.markdown("""
<style>

/* --------------------------------------------------
   MAIN APPLICATION
-------------------------------------------------- */

.stApp {
    background-color: #F7F9FC;
    color: #172033;
}

/* --------------------------------------------------
   TOP HEADER
-------------------------------------------------- */

header[data-testid="stHeader"] {
    background-color: transparent !important;
}

div[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
    position: fixed !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

div[data-testid="stStatusWidget"] {
    visibility: hidden !important;
}

/* --------------------------------------------------
   MAIN CONTENT WIDTH / SPACING
-------------------------------------------------- */

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1200px;
}

/* --------------------------------------------------
   SIDEBAR
-------------------------------------------------- */

section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0;
}

section[data-testid="stSidebar"] * {
    color: #172033;
}

section[data-testid="stSidebar"] a {
    color: #172033 !important;
}

section[data-testid="stSidebar"] a:hover {
    background-color: #F1F5F9 !important;
    border-radius: 8px;
}

/* --------------------------------------------------
   TYPOGRAPHY
-------------------------------------------------- */

h1 {
    color: #172033 !important;
    font-weight: 700 !important;
    letter-spacing: -0.6px;
}

h2 {
    color: #172033 !important;
    font-weight: 700 !important;
}

h3 {
    color: #172033 !important;
    font-weight: 600 !important;
}

p {
    color: #475569;
}

li {
    color: #475569;
}

/* --------------------------------------------------
   DIVIDERS
-------------------------------------------------- */

hr {
    border-color: #E2E8F0 !important;
}

/* --------------------------------------------------
   KPI / METRIC CARDS
-------------------------------------------------- */

div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px 22px;
    box-shadow: 0px 4px 14px rgba(15, 23, 42, 0.06);
    min-height: 120px;
}

div[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-weight: 500;
}

div[data-testid="stMetricValue"] {
    color: #172033 !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] > div {
    font-size: 1.9rem !important;
}

/* --------------------------------------------------
   HERO BADGE
-------------------------------------------------- */

.hero-badge {
    display: inline-block;
    background-color: #E6FFFB;
    color: #0F766E;
    padding: 7px 14px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 12px;
}

/* --------------------------------------------------
   INTRODUCTION CARD
-------------------------------------------------- */

.intro-box {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 5px solid #0EA5A8;
    border-radius: 14px;
    padding: 25px 28px;
    margin-top: 15px;
    margin-bottom: 30px;
    box-shadow: 0px 4px 14px rgba(15, 23, 42, 0.05);
}

.intro-box h3 {
    margin-top: 0;
    margin-bottom: 14px;
    color: #172033 !important;
}

.intro-box p {
    color: #475569;
    line-height: 1.7;
    margin-bottom: 10px;
}

/* --------------------------------------------------
   APPLICATION MODULE CARDS
-------------------------------------------------- */

.module-card {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0px 4px 14px rgba(15, 23, 42, 0.05);
    min-height: 170px;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.module-card:hover {
    transform: translateY(-2px);
    box-shadow: 0px 8px 20px rgba(15, 23, 42, 0.08);
}

.module-card p {
    color: #475569;
    line-height: 1.6;
}

.accent-title {
    color: #0EA5A8 !important;
    font-weight: 700 !important;
    margin-top: 0;
}

/* --------------------------------------------------
   BUSINESS OBJECTIVE BOX
-------------------------------------------------- */

.business-box {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 22px 25px;
    box-shadow: 0px 4px 14px rgba(15, 23, 42, 0.05);
}

.business-box p {
    color: #475569;
    line-height: 1.7;
}

.business-flow {
    color: #0F766E;
    font-weight: 700;
    font-size: 1.05rem;
    margin-top: 14px;
}

/* --------------------------------------------------
   FOOTER
-------------------------------------------------- */

.footer-text {
    color: #94A3B8;
    font-size: 0.85rem;
    text-align: center;
    margin-top: 25px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown(
    """
<div class="hero-badge">Customer Analytics &amp; Predictive Intelligence</div>
""",
    unsafe_allow_html=True
)

st.title("Telco Customer Churn Analytics")

st.markdown(
    """
<div class="intro-box">
<h3>Customer Retention &amp; Churn Intelligence</h3>
<p>A complete analytics solution combining business intelligence, customer segmentation and machine-learning based churn prediction.</p>
<p>Explore customer behaviour, understand churn drivers, identify high-risk customers and support targeted retention decisions.</p>
</div>
""",
    unsafe_allow_html=True
)

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

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

# ==========================================================
# APPLICATION MODULES
# ==========================================================

st.subheader("Application Modules")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
<div class="module-card">
<h3 class="accent-title">Churn Prediction</h3>
<p>Predict individual customer churn probability using the trained machine-learning model and assign each customer a churn-risk level.</p>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="module-card">
<h3 class="accent-title">Customer Segment &amp; Revenue</h3>
<p>Analyze customer value, revenue patterns, payment behaviour, tenure groups and important customer segments.</p>
</div>
""",
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
<div class="module-card">
<h3 class="accent-title">Business Analytics</h3>
<p>Explore churn KPIs, customer behaviour, service patterns and major business factors associated with customer churn.</p>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="module-card">
<h3 class="accent-title">High-Risk Customers</h3>
<p>Identify customers requiring immediate retention attention and review recommended actions that can support customer retention.</p>
</div>
""",
        unsafe_allow_html=True
    )

# ==========================================================
# BUSINESS OBJECTIVE
# ==========================================================

st.divider()

st.subheader("Business Objective")

st.markdown(
    """
<div class="business-box">
<p>The objective of this platform is to help a telecom business move beyond descriptive reporting toward proactive and data-driven customer retention.</p>
<div class="business-flow">Understand Churn → Identify Risk → Prioritize Customers → Take Action</div>
</div>
""",
    unsafe_allow_html=True
)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
<div class="footer-text">
Telco Churn Intelligence Platform
&nbsp; • &nbsp;
Python
&nbsp; • &nbsp;
Streamlit
&nbsp; • &nbsp;
Machine Learning
&nbsp; • &nbsp;
Power BI
&nbsp; • &nbsp;
Business Analytics
</div>
""",
    unsafe_allow_html=True
)
