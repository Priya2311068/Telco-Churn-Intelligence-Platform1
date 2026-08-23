import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = PROJECT_ROOT / "telco_churn_model.pkl"
PREPROCESSOR_PATH = PROJECT_ROOT / "telco_churn_preprocessor.pkl"
THRESHOLD_PATH = PROJECT_ROOT / "telco_churn_threshold.pkl"


# ============================================================
# LOAD MODEL COMPONENTS
# ============================================================

@st.cache_resource
def load_model_components():

    missing_files = []

    if not MODEL_PATH.exists():
        missing_files.append("telco_churn_model.pkl")

    if not PREPROCESSOR_PATH.exists():
        missing_files.append("telco_churn_preprocessor.pkl")

    if not THRESHOLD_PATH.exists():
        missing_files.append("telco_churn_threshold.pkl")

    if missing_files:
        raise FileNotFoundError(
            "Missing required model files: "
            + ", ".join(missing_files)
        )

    model = joblib.load(MODEL_PATH)

    preprocessor = joblib.load(
        PREPROCESSOR_PATH
    )

    threshold = joblib.load(
        THRESHOLD_PATH
    )

    threshold = float(
        np.asarray(threshold).squeeze()
    )

    return model, preprocessor, threshold


try:

    model, preprocessor, threshold = (
        load_model_components()
    )

except Exception as e:

    st.error(
        "⚠️ Unable to load the churn prediction model."
    )

    st.exception(e)

    st.stop()


# ============================================================
# PAGE THEME
# ============================================================

st.markdown("""
<style>

/* =========================================================
   MAIN PAGE
========================================================= */

.stApp {
    background-color: #F8FAFC;
    color: #16324F;
}


/* =========================================================
   REMOVE STREAMLIT TOP BAR
========================================================= */

header[data-testid="stHeader"] {
    background-color: transparent !important;
}

div[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0px !important;
}

div[data-testid="stDecoration"] {
    display: none !important;
}

div[data-testid="stStatusWidget"] {
    visibility: hidden !important;
}


/* =========================================================
   PAGE WIDTH
========================================================= */

.block-container {
    padding-top: 1.6rem !important;
    padding-bottom: 3rem !important;
    max-width: 1200px;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #DCE6F0;
}

section[data-testid="stSidebar"] * {
    color: #16324F;
}


/* =========================================================
   TITLES
========================================================= */

h1 {
    color: #0F2F4F !important;
    font-weight: 750 !important;
    letter-spacing: -0.6px;
}

h2,
h3 {
    color: #16324F !important;
    font-weight: 650 !important;
}

p {
    color: #526579;
}


/* =========================================================
   DIVIDER
========================================================= */

hr {
    border-color: #DCE6F0 !important;
}


/* =========================================================
   INPUT LABELS
========================================================= */

label {
    color: #24445F !important;
    font-weight: 600 !important;
}


/* =========================================================
   TEXT / NUMBER INPUTS
========================================================= */

div[data-baseweb="input"] {
    background-color: #FFFFFF !important;
    border-radius: 8px !important;
}

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background-color: #FFFFFF !important;
    color: #16324F !important;
    border: 1px solid #CAD8E5 !important;
}


/* =========================================================
   SELECT BOXES
========================================================= */

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #CAD8E5 !important;
    border-radius: 8px !important;
    color: #16324F !important;
}


/* =========================================================
   SELECT DROPDOWN TEXT
========================================================= */

div[data-baseweb="select"] span {
    color: #16324F !important;
}


/* =========================================================
   METRIC CARDS
========================================================= */

div[data-testid="stMetric"] {

    background-color: #FFFFFF;

    border: 1px solid #D7E2EC;

    border-radius: 10px;

    padding: 20px 22px;

    box-shadow:
        0px 5px 14px
        rgba(15, 47, 79, 0.10);
}


/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #526579 !important;
    font-weight: 600 !important;
}


/* Metric values */
div[data-testid="stMetricValue"] {
    color: #124F86 !important;
    font-weight: 750 !important;
}


/* =========================================================
   PREDICT BUTTON
========================================================= */

div.stButton > button {

    background-color: #12558D !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 8px !important;

    font-weight: 650 !important;

    min-height: 48px;

    box-shadow:
        0px 4px 10px
        rgba(18, 85, 141, 0.20);

    transition: 0.2s ease;
}


div.stButton > button:hover {

    background-color: #0C4778 !important;

    box-shadow:
        0px 7px 16px
        rgba(18, 85, 141, 0.25);

    transform: translateY(-1px);
}


/* =========================================================
   DATAFRAME
========================================================= */

div[data-testid="stDataFrame"] {

    background-color: #FFFFFF;

    border: 1px solid #D7E2EC;

    border-radius: 10px;

    overflow: hidden;

    box-shadow:
        0px 4px 12px
        rgba(15, 47, 79, 0.07);
}


/* =========================================================
   INFO BOX
========================================================= */

div[data-testid="stAlert"] {
    border-radius: 8px;
}


/* =========================================================
   CUSTOM INTRO CARD
========================================================= */

.prediction-intro {

    background-color: #FFFFFF;

    border: 1px solid #D7E2EC;

    border-left: 5px solid #168CE3;

    border-radius: 10px;

    padding: 20px 24px;

    margin-top: 12px;

    margin-bottom: 28px;

    box-shadow:
        0px 5px 14px
        rgba(15, 47, 79, 0.07);
}


.prediction-intro p {

    color: #526579;

    margin: 0;

    line-height: 1.7;
}


/* =========================================================
   SMALL PAGE BADGE
========================================================= */

.prediction-badge {

    display: inline-block;

    background-color: #E9F4FD;

    color: #12558D;

    border: 1px solid #CDE6FA;

    padding: 6px 13px;

    border-radius: 999px;

    font-size: 0.84rem;

    font-weight: 650;

    margin-bottom: 10px;
}


/* =========================================================
   SECTION LABEL
========================================================= */

.section-label {

    color: #168CE3;

    font-size: 0.76rem;

    font-weight: 750;

    text-transform: uppercase;

    letter-spacing: 0.08em;

    margin-bottom: 2px;
}


/* =========================================================
   SECTION CARD LOOK
========================================================= */

.section-note {

    background-color: #FFFFFF;

    border: 1px solid #DCE6F0;

    border-radius: 10px;

    padding: 10px 14px;

    margin-bottom: 12px;
}


/* =========================================================
   HIGH-RISK RESULT
========================================================= */

.high-risk-box {

    background-color: #FFF1F2;

    border-left: 5px solid #D94452;

    color: #991B1B;

    padding: 15px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin-top: 15px;
}


/* =========================================================
   MEDIUM RISK RESULT
========================================================= */

.medium-risk-box {

    background-color: #FFF7E6;

    border-left: 5px solid #F59E0B;

    color: #92400E;

    padding: 15px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin-top: 15px;
}


/* =========================================================
   LOW RISK RESULT
========================================================= */

.low-risk-box {

    background-color: #ECFDF5;

    border-left: 5px solid #10B981;

    color: #065F46;

    padding: 15px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin-top: 15px;
}


/* =========================================================
   RECOMMENDATION CARD
========================================================= */

.recommendation-box {

    background-color: #EDF6FD;

    border-left: 5px solid #12558D;

    color: #16324F;

    padding: 18px 20px;

    border-radius: 8px;

    margin-top: 8px;

    margin-bottom: 20px;
}


/* =========================================================
   FOOTER
========================================================= */

.footer-text {

    text-align: center;

    color: #8A9AAC;

    font-size: 0.83rem;

    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    """
<div class="prediction-badge">
Predictive Customer Intelligence
</div>
""",
    unsafe_allow_html=True
)

st.title(
    "Customer Churn Prediction"
)

st.markdown(
    """
<div class="prediction-intro">
<p>
Predict customer churn probability using the trained
<strong>Logistic Regression model</strong>. Enter customer
demographic, account and service details to estimate churn
risk and generate an appropriate retention recommendation.
</p>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INPUT
# ============================================================

st.markdown(
    '<div class="section-label">Customer Profile</div>',
    unsafe_allow_html=True
)

st.subheader(
    "👤 Customer Information"
)

col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    tenure = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

    cltv = st.number_input(
        "CLTV",
        min_value=0.0,
        value=4500.0
    )


# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Female",
            "Male"
        ]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [
            "No",
            "Yes"
        ]
    )

    partner = st.selectbox(
        "Partner",
        [
            "No",
            "Yes"
        ]
    )

    dependents = st.selectbox(
        "Dependents",
        [
            "No",
            "Yes"
        ]
    )


# ------------------------------------------------------------
# COLUMN 3
# ------------------------------------------------------------

with col3:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        [
            "No",
            "Yes"
        ]
    )


# ============================================================
# SERVICE INFORMATION
# ============================================================

st.markdown(
    '<div class="section-label">Subscription Details</div>',
    unsafe_allow_html=True
)

st.subheader(
    "🌐 Service Information"
)

col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    phone_service = st.selectbox(
        "Phone Service",
        [
            "No",
            "Yes"
        ]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )


# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    online_security = st.selectbox(
        "Online Security",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


# ------------------------------------------------------------
# COLUMN 3
# ------------------------------------------------------------

with col3:

    device_protection = st.selectbox(
        "Device Protection",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


# ============================================================
# ENTERTAINMENT SERVICES
# ============================================================

st.markdown(
    '<div class="section-label">Media Services</div>',
    unsafe_allow_html=True
)

st.subheader(
    "📺 Entertainment Services"
)

col1, col2 = st.columns(2)


with col1:

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


with col2:

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


# ============================================================
# LOCATION
# ============================================================

st.markdown(
    '<div class="section-label">Geographic Information</div>',
    unsafe_allow_html=True
)

st.subheader(
    "📍 Customer Location"
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    latitude = st.number_input(
        "Latitude",
        value=36.7783,
        format="%.6f"
    )


with col2:

    longitude = st.number_input(
        "Longitude",
        value=-119.4179,
        format="%.6f"
    )


with col3:

    country = st.text_input(
        "Country",
        value="United States"
    )


with col4:

    state = st.text_input(
        "State",
        value="California"
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "Predict Churn Risk",
    width="stretch"
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    input_data = pd.DataFrame(
        {
            "Latitude": [
                latitude
            ],

            "Longitude": [
                longitude
            ],

            "Country": [
                country
            ],

            "State": [
                state
            ],

            "Gender": [
                gender
            ],

            "Senior Citizen": [
                senior_citizen
            ],

            "Partner": [
                partner
            ],

            "Dependents": [
                dependents
            ],

            "Tenure Months": [
                tenure
            ],

            "Phone Service": [
                phone_service
            ],

            "Multiple Lines": [
                multiple_lines
            ],

            "Internet Service": [
                internet_service
            ],

            "Online Security": [
                online_security
            ],

            "Online Backup": [
                online_backup
            ],

            "Device Protection": [
                device_protection
            ],

            "Tech Support": [
                tech_support
            ],

            "Streaming TV": [
                streaming_tv
            ],

            "Streaming Movies": [
                streaming_movies
            ],

            "Contract": [
                contract
            ],

            "Paperless Billing": [
                paperless_billing
            ],

            "Payment Method": [
                payment_method
            ],

            "Monthly Charges": [
                monthly_charges
            ],

            "Total Charges": [
                total_charges
            ],

            "CLTV": [
                cltv
            ]
        }
    )


    # ========================================================
    # MODEL PREDICTION
    # ========================================================

    try:

        X_processed = (
            preprocessor.transform(
                input_data
            )
        )

        churn_probability = (
            model.predict_proba(
                X_processed
            )[0][1]
        )

    except Exception as e:

        st.error(
            "⚠️ An error occurred while generating the prediction."
        )

        st.exception(e)

        st.stop()


    # ========================================================
    # APPLY THRESHOLD
    # ========================================================

    prediction = int(
        churn_probability >= threshold
    )

    probability_percent = (
        churn_probability * 100
    )


    st.divider()


    # ========================================================
    # RESULT
    # ========================================================

    st.markdown(
        '<div class="section-label">Model Output</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        "Prediction Result"
    )

    result_col1, result_col2, result_col3 = (
        st.columns(3)
    )


    with result_col1:

        st.metric(
            "Churn Probability",
            f"{probability_percent:.2f}%"
        )


    with result_col2:

        st.metric(
            "Decision Threshold",
            f"{threshold:.2f}"
        )


    with result_col3:

        if prediction == 1:

            st.metric(
                "Prediction",
                "HIGH RISK"
            )

        else:

            st.metric(
                "Prediction",
                "LOW RISK"
            )


    # ========================================================
    # RISK LEVEL
    # ========================================================

    if probability_percent >= 70:

        risk_level = "High Risk"

        recommendation = (
            "Contract upgrade + "
            "security/service retention offer"
        )

        st.markdown(
            """
<div class="high-risk-box">
High Risk — Immediate retention action recommended.
</div>
""",
            unsafe_allow_html=True
        )


    elif probability_percent >= 40:

        risk_level = "Medium Risk"

        recommendation = (
            "Targeted retention campaign and "
            "monitor customer behavior"
        )

        st.markdown(
            """
<div class="medium-risk-box">
Medium Risk — Customer should be monitored closely.
</div>
""",
            unsafe_allow_html=True
        )


    else:

        risk_level = "Low Risk"

        recommendation = (
            "Monitor"
        )

        st.markdown(
            """
<div class="low-risk-box">
Low Risk — No immediate retention action required.
</div>
""",
            unsafe_allow_html=True
        )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.subheader(
        "Recommended Action"
    )

    st.markdown(
        f"""
<div class="recommendation-box">
<strong>{recommendation}</strong>
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # CUSTOMER SUMMARY
    # ========================================================

    st.subheader(
        "Customer Summary"
    )

    summary = pd.DataFrame(
        {
            "Feature": [
                "Contract",
                "Internet Service",
                "Tenure Months",
                "Monthly Charges",
                "Online Security",
                "Tech Support",
                "Payment Method",
                "Risk Level"
            ],

            "Value": [
                contract,
                internet_service,
                tenure,
                f"${monthly_charges:.2f}",
                online_security,
                tech_support,
                payment_method,
                risk_level
            ]
        }
    )


    summary["Value"] = (
        summary["Value"]
        .astype(str)
    )


    st.dataframe(
        summary,
        width="stretch",
        hide_index=True
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
Predictive Analytics
&nbsp; • &nbsp;
Logistic Regression
&nbsp; • &nbsp;
Customer Retention
</div>
""",
    unsafe_allow_html=True
)
