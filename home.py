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
# ============================================================

def html(content):
    st.html(dedent(content).strip())


# ============================================================
# PROFESSIONAL UI THEME
# ============================================================

html(
    """
    <style>

    /* ---------------- GLOBAL PAGE ---------------- */

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {
        background-color: #F6F8FB !important;
        color: #17233C !important;
        color-scheme: light !important;
    }

    .block-container {
        max-width: 1220px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
    }


    /* ---------------- STREAMLIT CLEANUP ---------------- */

    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 25px !important;
    }

    div[data-testid="stToolbar"] {
        visibility: hidden !important;
        height: 0 !important;
    }

    div[data-testid="stDecoration"],
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }


    /* ---------------- SIDEBAR ---------------- */

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #DCE5EE !important;
    }

    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] * {
        color: #17233C;
    }


    /* ---------------- PAGE BADGE ---------------- */

    .page-badge {
        display: inline-flex;
        align-items: center;

        background: #E6F7F5;
        color: #087F73;

        border: 1px solid #C7ECE8;
        border-radius: 999px;

        padding: 7px 16px;

        font-size: 0.82rem;
        font-weight: 700;

        margin-bottom: 22px;
    }


    /* ---------------- BRAND HEADER ---------------- */

    .brand-header {
        display: flex;
        align-items: center;
        gap: 18px;

        margin-bottom: 28px;
    }

    .brand-logo {
        width: 64px;
        height: 64px;
        min-width: 64px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 16px;

        background:
            linear-gradient(
                135deg,
                #145B8F,
                #168CE3
            );

        box-shadow:
            0 8px 22px rgba(20, 91, 143, 0.20);

        font-size: 31px;
    }

    .brand-title {
        color: #17233C;

        font-size: 2.55rem;
        line-height: 1.05;

        font-weight: 780;
        letter-spacing: -0.9px;

        margin: 0;
    }

    .brand-subtitle {
        color: #64748B;

        font-size: 0.76rem;
        margin-top: 8px;

        letter-spacing: 0.08em;
        font-weight: 650;
    }


    /* ---------------- HERO CARD ---------------- */

    .hero-card {
        background: #FFFFFF;

        border: 1px solid #D8E2EC;
        border-left: 5px solid #16A6A1;

        border-radius: 14px;

        padding: 30px 32px;

        margin-bottom: 28px;

        box-shadow:
            0 6px 20px rgba(15, 47, 79, 0.06);
    }

    .hero-label {
        color: #087F73;

        font-size: 0.77rem;
        font-weight: 750;

        letter-spacing: 0.08em;

        margin-bottom: 9px;
    }

    .hero-card h2 {
        color: #17233C;

        margin: 0 0 12px 0;

        font-size: 1.72rem;
        font-weight: 760;
    }

    .hero-card p {
        color: #52657A;

        line-height: 1.7;

        margin: 0;

        font-size: 0.98rem;

        max-width: 900px;
    }


    /* ---------------- SECTION TITLE ---------------- */

    .section-title {
        color: #17233C;

        font-size: 1.45rem;
        font-weight: 750;

        margin-top: 6px;
        margin-bottom: 16px;
    }

    .section-subtitle {
        color: #718096;

        font-size: 0.92rem;

        margin-top: -10px;
        margin-bottom: 22px;
    }


    /* ---------------- BUSINESS KPI CARDS ---------------- */

    .kpi-grid {
        display: grid;

        grid-template-columns:
            repeat(4, minmax(0, 1fr));

        gap: 16px;

        margin-bottom: 32px;
    }

    .kpi-card {
        background: #FFFFFF;

        border: 1px solid #D8E2EC;

        border-radius: 14px;

        padding: 20px 22px;

        min-height: 105px;

        box-shadow:
            0 4px 14px rgba(15, 47, 79, 0.05);

        position: relative;
        overflow: hidden;
    }

    .kpi-card::before {
        content: "";

        position: absolute;

        left: 0;
        top: 0;

        width: 4px;
        height: 100%;

        background: #16A6A1;
    }

    .kpi-label {
        color: #718096;

        font-size: 0.78rem;
        font-weight: 650;

        margin-bottom: 9px;
    }

    .kpi-value {
        color: #17233C;

        font-size: 1.75rem;
        line-height: 1.1;

        font-weight: 780;
    }

    .kpi-note {
        color: #8A9AAD;

        font-size: 0.72rem;

        margin-top: 7px;
    }


    /* ---------------- WORKFLOW ---------------- */

    .workflow {
        display: grid;

        grid-template-columns:
            1fr 38px 1fr 38px 1fr 38px 1fr;

        align-items: center;

        margin-bottom: 35px;
    }

    .workflow-card {
        background: #FFFFFF;

        border: 1px solid #D8E2EC;

        border-radius: 12px;

        padding: 18px 12px;

        text-align: center;

        min-height: 100px;

        box-shadow:
            0 4px 12px rgba(15, 47, 79, 0.04);
    }

    .workflow-icon {
        font-size: 1.45rem;

        margin-bottom: 7px;
    }

    .workflow-title {
        color: #17233C;

        font-weight: 730;

        font-size: 0.92rem;

        margin-bottom: 4px;
    }

    .workflow-text {
        color: #718096;

        font-size: 0.74rem;

        line-height: 1.4;
    }

    .workflow-arrow {
        text-align: center;

        color: #16A6A1;

        font-size: 1.4rem;

        font-weight: 800;
    }


    /* ---------------- MODULE CARDS ---------------- */

    .module-card {
        background: #FFFFFF;

        border: 1px solid #D8E2EC;

        border-radius: 14px;

        padding: 23px 25px;

        margin-bottom: 16px;

        min-height: 145px;

        box-shadow:
            0 4px 14px rgba(15, 47, 79, 0.05);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease,
            border-color 0.2s ease;
    }

    .module-card:hover {
        transform: translateY(-2px);

        border-color: #B8DAD7;

        box-shadow:
            0 8px 22px rgba(15, 47, 79, 0.08);
    }

    .module-icon {
        width: 38px;
        height: 38px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: #EEF7FA;

        border-radius: 10px;

        font-size: 1.15rem;

        margin-bottom: 14px;
    }

    .module-card h3 {
        color: #145B8F;

        margin: 0 0 8px 0;

        font-size: 1.08rem;
        font-weight: 740;
    }

    .module-card p {
        color: #5C6F82;

        line-height: 1.6;

        margin: 0;

        font-size: 0.91rem;
    }


    /* ---------------- TECH STRIP ---------------- */

    .tech-strip {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;

        gap: 10px;

        margin-top: 4px;
    }

    .tech-pill {
        background: #EEF3F8;

        color: #52657A;

        border: 1px solid #DCE5EE;

        border-radius: 999px;

        padding: 6px 13px;

        font-size: 0.75rem;
        font-weight: 650;
    }


    /* ---------------- FOOTER ---------------- */

    .footer-text {
        text-align: center;

        color: #8797A8;

        font-size: 0.79rem;

        margin-top: 24px;
        padding-bottom: 10px;
    }


    hr {
        border-color: #DCE5EE !important;

        margin-top: 1.7rem !important;
        margin-bottom: 1.7rem !important;
    }


    /* ---------------- RESPONSIVE ---------------- */

    @media (max-width: 900px) {

        .kpi-grid {
            grid-template-columns:
                repeat(2, minmax(0, 1fr));
        }

        .workflow {
            grid-template-columns: 1fr;
            gap: 10px;
        }

        .workflow-arrow {
            transform: rotate(90deg);
        }

    }


    @media (max-width: 600px) {

        .kpi-grid {
            grid-template-columns: 1fr;
        }

        .brand-title {
            font-size: 2rem;
        }

        .brand-logo {
            width: 52px;
            height: 52px;
            min-width: 52px;

            font-size: 26px;
        }

    }

    </style>
    """
)


# ============================================================
# BADGE
# ============================================================

html(
    """
    <div class="page-badge">
        Customer Analytics &amp; Predictive Intelligence
    </div>
    """
)


# ============================================================
# BRAND HEADER
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
# HERO SECTION
# ============================================================

html(
    """
    <div class="hero-card">

        <div class="hero-label">
            CUSTOMER RETENTION INTELLIGENCE
        </div>

        <h2>
            Turn Customer Data Into Retention Decisions
        </h2>

        <p>
            Analyze customer behaviour, uncover churn drivers,
            predict individual churn risk and identify customers
            requiring targeted retention action — all within one
            interactive analytics application.
        </p>

    </div>
    """
)


# ============================================================
# BUSINESS OVERVIEW
# ============================================================

html(
    """
    <div class="section-title">
        Business Overview
    </div>

    <div class="section-subtitle">
        Key customer and churn indicators from the Telco dataset.
    </div>
    """
)


html(
    """
    <div class="kpi-grid">

        <div class="kpi-card">
            <div class="kpi-label">
                TOTAL CUSTOMERS
            </div>

            <div class="kpi-value">
                7,043
            </div>

            <div class="kpi-note">
                Customer base analyzed
            </div>
        </div>


        <div class="kpi-card">
            <div class="kpi-label">
                CHURN RATE
            </div>

            <div class="kpi-value">
                26.54%
            </div>

            <div class="kpi-note">
                Overall customer churn
            </div>
        </div>


        <div class="kpi-card">
            <div class="kpi-label">
                CHURNED CUSTOMERS
            </div>

            <div class="kpi-value">
                1,869
            </div>

            <div class="kpi-note">
                Customers requiring analysis
            </div>
        </div>


        <div class="kpi-card">
            <div class="kpi-label">
                ML DECISION THRESHOLD
            </div>

            <div class="kpi-value">
                0.62
            </div>

            <div class="kpi-note">
                Logistic Regression
            </div>
        </div>

    </div>
    """
)


# ============================================================
# ANALYTICS WORKFLOW
# ============================================================

html(
    """
    <div class="section-title">
        From Data to Retention Action
    </div>

    <div class="section-subtitle">
        The application connects business analytics with predictive
        modelling to support customer-retention decisions.
    </div>
    """
)


html(
    """
    <div class="workflow">

        <div class="workflow-card">

            <div class="workflow-icon">
                📊
            </div>

            <div class="workflow-title">
                Analyze
            </div>

            <div class="workflow-text">
                Understand churn patterns
                and customer behaviour
            </div>

        </div>


        <div class="workflow-arrow">
            →
        </div>


        <div class="workflow-card">

            <div class="workflow-icon">
                🎯
            </div>

            <div class="workflow-title">
                Predict
            </div>

            <div class="workflow-text">
                Estimate individual
                customer churn probability
            </div>

        </div>


        <div class="workflow-arrow">
            →
        </div>


        <div class="workflow-card">

            <div class="workflow-icon">
                🚨
            </div>

            <div class="workflow-title">
                Prioritize
            </div>

            <div class="workflow-text">
                Identify customers with
                elevated churn risk
            </div>

        </div>


        <div class="workflow-arrow">
            →
        </div>


        <div class="workflow-card">

            <div class="workflow-icon">
                💡
            </div>

            <div class="workflow-title">
                Act
            </div>

            <div class="workflow-text">
                Support targeted
                retention strategies
            </div>

        </div>

    </div>
    """
)


# ============================================================
# APPLICATION MODULES
# ============================================================

html(
    """
    <div class="section-title">
        Explore the Application
    </div>

    <div class="section-subtitle">
        Navigate through the modules to investigate churn,
        customer value and retention opportunities.
    </div>
    """
)


col1, col2 = st.columns(2, gap="medium")


with col1:

    html(
        """
        <div class="module-card">

            <div class="module-icon">
                🎯
            </div>

            <h3>
                Churn Prediction
            </h3>

            <p>
                Estimate an individual customer's churn probability
                using the trained Logistic Regression model and
                generate risk-based retention recommendations.
            </p>

        </div>
        """
    )


    html(
        """
        <div class="module-card">

            <div class="module-icon">
                💰
            </div>

            <h3>
                Customer Segments &amp; Revenue
            </h3>

            <p>
                Analyze customer value, revenue patterns,
                tenure groups and payment behaviour to understand
                commercially important customer segments.
            </p>

        </div>
        """
    )


with col2:

    html(
        """
        <div class="module-card">

            <div class="module-icon">
                📊
            </div>

            <h3>
                Churn Analytics
            </h3>

            <p>
                Explore churn KPIs, behavioural patterns and
                major churn drivers through interactive
                business analytics.
            </p>

        </div>
        """
    )


    html(
        """
        <div class="module-card">

            <div class="module-icon">
                🚨
            </div>

            <h3>
                High-Risk Customers
            </h3>

            <p>
                Identify customers requiring immediate attention,
                inspect their risk profiles and review recommended
                retention actions.
            </p>

        </div>
        """
    )


# ============================================================
# TECHNOLOGY
# ============================================================

st.divider()

html(
    """
    <div class="tech-strip">

        <div class="tech-pill">
            Python
        </div>

        <div class="tech-pill">
            Streamlit
        </div>

        <div class="tech-pill">
            Scikit-learn
        </div>

        <div class="tech-pill">
            Logistic Regression
        </div>

        <div class="tech-pill">
            Business Intelligence
        </div>

        <div class="tech-pill">
            Predictive Analytics
        </div>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

html(
    """
    <div class="footer-text">
        Telco Churn Intelligence Platform
        &nbsp; • &nbsp;
        Customer Analytics &amp; Predictive Intelligence
    </div>
    """
)
