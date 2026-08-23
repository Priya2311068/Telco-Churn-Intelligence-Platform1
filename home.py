import streamlit as st


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
# PROFESSIONAL LIGHT THEME
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       GLOBAL PAGE
    -------------------------------------------------------- */

    .stApp {
        background-color: #F7F9FC;
        color: #16324F;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }


    /* --------------------------------------------------------
       HIDE STREAMLIT TOP BAR
    -------------------------------------------------------- */

    header[data-testid="stHeader"] {
        background: transparent;
    }

    div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0;
    }

    div[data-testid="stDecoration"] {
        display: none;
    }

    div[data-testid="stStatusWidget"] {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #D7E2EC;
    }

    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] * {
        color: #16324F;
    }


    /* --------------------------------------------------------
       PAGE BADGE
    -------------------------------------------------------- */

    .page-badge {
        display: inline-block;

        background: #E3F8F5;
        color: #087F73;

        border-radius: 999px;

        padding: 7px 16px;

        font-size: 0.84rem;
        font-weight: 650;

        margin-bottom: 25px;
    }


    /* --------------------------------------------------------
       MAIN LOGO + HEADING
    -------------------------------------------------------- */

    .brand-header {
        display: flex;
        align-items: center;
        gap: 18px;

        margin-bottom: 28px;
    }


    .brand-logo {
        width: 62px;
        height: 62px;

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

        font-size: 34px;

        flex-shrink: 0;
    }


    .brand-title {
        color: #17233C;

        font-size: 2.65rem;

        line-height: 1.1;

        font-weight: 750;

        letter-spacing: -1px;

        margin: 0;
    }


    .brand-subtitle {
        color: #64748B;

        font-size: 0.85rem;

        margin-top: 5px;

        letter-spacing: 0.03em;
    }


    /* --------------------------------------------------------
       INTRO CARD
    -------------------------------------------------------- */

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
    }


    .intro-card p {
        color: #52657A;

        line-height: 1.7;

        margin-bottom: 10px;

        font-size: 1rem;
    }


    /* --------------------------------------------------------
       SECTION HEADINGS
    -------------------------------------------------------- */

    .section-title {
        color: #17233C;

        font-size: 1.65rem;

        font-weight: 700;

        margin-top: 10px;

        margin-bottom: 18px;
    }


    /* --------------------------------------------------------
       STREAMLIT METRIC CARDS
    -------------------------------------------------------- */

    [data-testid="stMetric"] {
        background: #FFFFFF;

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


    /* --------------------------------------------------------
       MODULE CARDS
    -------------------------------------------------------- */

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

        font-size: 1.18rem;
    }


    .module-card p {
        color: #5C6F82;

        line-height: 1.65;

        margin-bottom: 0;
    }


    /* --------------------------------------------------------
       DIVIDERS
    -------------------------------------------------------- */

    hr {
        border-color: #DCE5EE !important;

        margin-top: 2rem !important;

        margin-bottom: 2rem !important;
    }


    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer-text {
        text-align: center;

        color: #8797A8;

        font-size: 0.82rem;

        margin-top: 22px;
    }


    /* --------------------------------------------------------
       RESPONSIVE HEADER
    -------------------------------------------------------- */

    @media (max-width: 800px) {

        .brand-logo {
            width: 52px;
            height: 52px;

            font-size: 28px;
        }

        .brand-title {
            font-size: 2rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE BADGE
# ============================================================

st.markdown(
    """
    <div class="page-badge">
        Customer Analytics & Predictive Intelligence
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TELCO BRAND HEADER
# ============================================================

st.markdown(
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
                CUSTOMER RETENTION • REVENUE RISK •
                PREDICTIVE INTELLIGENCE
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    <div class="intro-card">

        <h2>
            Customer Retention & Churn Intelligence
        </h2>

        <p>
            A complete analytics solution combining business
            intelligence, customer segmentation and
            machine-learning based churn prediction.
        </p>

        <p>
            Explore customer behaviour, understand churn drivers,
            identify high-risk customers and support targeted
            retention decisions.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Project Overview
    </div>
    """,
    unsafe_allow_html=True
)


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


# ============================================================
# APPLICATION MODULES
# ============================================================

st.markdown(
    """
    <div class="section-title">
        Application Modules
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    st.markdown(
        """
        <div class="module-card">

            <h3>
                🔮 Churn Prediction
            </h3>

            <p>
                Predict individual customer churn probability
                using the trained machine-learning model and
                generate targeted retention recommendations.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="module-card">

            <h3>
                💰 Customer Segment & Revenue
            </h3>

            <p>
                Analyze customer value, revenue patterns,
                payment behaviour, tenure groups and
                customer segments.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    st.markdown(
        """
        <div class="module-card">

            <h3>
                📊 Business Analytics
            </h3>

            <p>
                Explore churn KPIs, customer behaviour,
                churn drivers and important business
                insights through interactive analytics.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="module-card">

            <h3>
                🚨 High Risk Customers
            </h3>

            <p>
                Identify customers requiring immediate
                retention attention and review recommended
                retention actions.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()


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
        Business Analytics

    </div>
    """,
    unsafe_allow_html=True
)
