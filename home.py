import streamlit as st
from textwrap import dedent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Telco Churn Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# HTML HELPER
# Prevents HTML from appearing as plain/code text
# ============================================================

def html(content):
    st.html(
        dedent(content).strip()
    )


# ============================================================
# PROFESSIONAL LIGHT THEME
# ============================================================

html(
    """
    <style>

    /* ======================================================
       GLOBAL PAGE
    ====================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {

        background-color: #F7F9FC !important;

        color: #16324F !important;

        color-scheme: light !important;
    }


    /* ======================================================
       MAIN CONTENT AREA
    ====================================================== */

    .block-container {

        max-width: 1200px !important;

        padding-top: 1.3rem !important;

        padding-bottom: 3rem !important;
    }


    /* ======================================================
       STREAMLIT HEADER
    ====================================================== */

    header[data-testid="stHeader"] {

        background: transparent !important;

        height: 25px !important;
    }


    div[data-testid="stToolbar"] {

        visibility: hidden !important;

        height: 0 !important;
    }


    div[data-testid="stDecoration"] {

        display: none !important;
    }


    div[data-testid="stStatusWidget"] {

        visibility: hidden !important;
    }


    #MainMenu {

        visibility: hidden;
    }


    footer {

        visibility: hidden;
    }


    /* ======================================================
       SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {

        background-color: #FFFFFF !important;

        border-right: 1px solid #D7E2EC !important;
    }


    section[data-testid="stSidebar"] > div {

        background-color: #FFFFFF !important;
    }


    section[data-testid="stSidebar"] * {

        color: #16324F;
    }


    /* ======================================================
       PAGE BADGE
    ====================================================== */

    .page-badge {

        display: inline-block;

        background: #E3F8F5;

        color: #087F73;

        border: 1px solid #C7EFEA;

        border-radius: 999px;

        padding: 7px 16px;

        font-size: 0.84rem;

        font-weight: 650;

        margin-bottom: 22px;
    }


    /* ======================================================
       MAIN BRAND HEADER
    ====================================================== */

    .brand-header {

        display: flex;

        align-items: center;

        gap: 18px;

        margin-bottom: 30px;
    }


    .brand-logo {

        width: 64px;

        height: 64px;

        min-width: 64px;

        display: flex;

        align-items: center;

        justify-content: center;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                #145B8F,
                #168CE3
            );

        box-shadow:
            0 5px 14px
            rgba(20, 91, 143, 0.20);

        font-size: 33px;
    }


    .brand-title {

        color: #17233C;

        font-size: 2.55rem;

        line-height: 1.05;

        font-weight: 760;

        letter-spacing: -0.8px;

        margin: 0;
    }


    .brand-subtitle {

        color: #64748B;

        font-size: 0.78rem;

        margin-top: 7px;

        letter-spacing: 0.06em;

        font-weight: 600;
    }


    /* ======================================================
       INTRO CARD
    ====================================================== */

    .intro-card {

        background: #FFFFFF;

        border: 1px solid #D8E2EC;

        border-left: 5px solid #16A6A1;

        border-radius: 12px;

        padding: 28px 30px;

        margin-bottom: 38px;

        box-shadow:
            0 5px 15px
            rgba(15, 47, 79, 0.06);
    }


    .intro-card h2 {

        color: #17233C;

        margin-top: 0;

        margin-bottom: 22px;

        font-size: 1.65rem;

        font-weight: 720;
    }


    .intro-card p {

        color: #52657A;

        line-height: 1.7;

        margin-top: 0;

        margin-bottom: 12px;

        font-size: 1rem;
    }


    .intro-card p:last-child {

        margin-bottom: 0;
    }


    /* ======================================================
       SECTION TITLES
    ====================================================== */

    .section-title {

        color: #17233C;

        font-size: 1.65rem;

        font-weight: 720;

        margin-top: 5px;

        margin-bottom: 18px;
    }


    /* ======================================================
       PROJECT OVERVIEW CARDS
    ====================================================== */

    [data-testid="stMetric"] {

        background: #FFFFFF !important;

        border: 1px solid #D8E2EC;

        border-radius: 12px;

        padding: 22px 24px;

        min-height: 128px;

        box-shadow:
            0 5px 14px
            rgba(15, 47, 79, 0.06);
    }


    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] * {

        color: #64748B !important;
    }


    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {

        color: #43576D !important;

        font-weight: 750 !important;
    }


    /* ======================================================
       APPLICATION MODULE CARDS
    ====================================================== */

    .module-card {

        background: #FFFFFF;

        border: 1px solid #D8E2EC;

        border-radius: 12px;

        padding: 24px 26px;

        margin-bottom: 18px;

        min-height: 150px;

        box-shadow:
            0 4px 12px
            rgba(15, 47, 79, 0.05);
    }


    .module-card h3 {

        color: #145B8F;

        margin-top: 0;

        margin-bottom: 10px;

        font-size: 1.18rem;

        font-weight: 720;
    }


    .module-card p {

        color: #5C6F82;

        line-height: 1.65;

        margin: 0;
    }


    /* ======================================================
       DIVIDER
    ====================================================== */

    hr {

        border-color: #DCE5EE !important;

        margin-top: 2rem !important;

        margin-bottom: 2rem !important;
    }


    /* ======================================================
       FOOTER
    ====================================================== */

    .footer-text {

        text-align: center;

        color: #8797A8;

        font-size: 0.82rem;

        margin-top: 22px;

        padding-bottom: 10px;
    }


    /* ======================================================
       RESPONSIVE DESIGN
    ====================================================== */

    @media (max-width: 800px) {

        .brand-header {

            gap: 12px;
        }


        .brand-logo {

            width: 52px;

            height: 52px;

            min-width: 52px;

            font-size: 27px;
        }


        .brand-title {

            font-size: 2rem;
        }


        .brand-subtitle {

            font-size: 0.68rem;
        }

    }

    </style>
    """
)


# ============================================================
# PAGE BADGE
# ============================================================

html(
    """
    <div class="page-badge">
        Customer Analytics &amp; Predictive Intelligence
    </div>
    """
)


# ============================================================
# MAIN BRAND HEADER
# ============================================================

html(
    """
    <div class="brand-header">

        <div class="brand-logo">
            📡
        </div>

        <div>

            <h1 class="brand-title">
                Telco Customer Churn Analytics
            </h1>

            <div class="brand-subtitle">
                CUSTOMER RETENTION • REVENUE RISK • PREDICTIVE INTELLIGENCE
            </div>

        </div>

    </div>
    """
)


# ============================================================
# INTRODUCTION CARD
# ============================================================

html(
    """
    <div class="intro-card">

        <h2>
            Customer Retention &amp; Churn Intelligence
        </h2>

        <p>
            A complete analytics solution combining business intelligence,
            customer segmentation and machine-learning based churn prediction.
        </p>

        <p>
            Explore customer behaviour, understand churn drivers,
            identify high-risk customers and support targeted
            retention decisions.
        </p>

    </div>
    """
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

html(
    """
    <div class="section-title">
        Project Overview
    </div>
    """
)


col1, col2, col3 = st.columns(
    3,
    gap="medium"
)


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


# ============================================================
# APPLICATION MODULES
# ============================================================

html(
    """
    <div class="section-title">
        Application Modules
    </div>
    """
)


col1, col2 = st.columns(
    2,
    gap="medium"
)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    html(
        """
        <div class="module-card">

            <h3>
                🔮 Churn Prediction
            </h3>

            <p>
                Predict individual customer churn probability using
                the trained machine-learning model and generate
                targeted retention recommendations.
            </p>

        </div>
        """
    )


    html(
        """
        <div class="module-card">

            <h3>
                💰 Customer Segment &amp; Revenue
            </h3>

            <p>
                Analyze customer value, revenue patterns,
                payment behaviour, tenure groups and
                customer segments.
            </p>

        </div>
        """
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    html(
        """
        <div class="module-card">

            <h3>
                📊 Business Analytics
            </h3>

            <p>
                Explore churn KPIs, customer behaviour,
                churn drivers and important business insights
                through interactive analytics.
            </p>

        </div>
        """
    )


    html(
        """
        <div class="module-card">

            <h3>
                🚨 High Risk Customers
            </h3>

            <p>
                Identify customers requiring immediate retention
                attention and review recommended retention actions.
            </p>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()


html(
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
        Business Analytics

    </div>
    """
)
