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
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    threshold = joblib.load(THRESHOLD_PATH)

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
# PROFESSIONAL LIGHT DASHBOARD THEME
# ============================================================

st.markdown(
    """
<style>

/* ==========================================================
   MASTER COLOR SYSTEM
========================================================== */

:root {

    --page-bg: #F7F9FC;
    --card-bg: #FFFFFF;

    --navy: #103A5E;
    --text: #16324F;
    --muted: #526579;

    --blue: #145B8F;
    --blue-hover: #0E4B78;
    --bright-blue: #168CE3;

    --border: #C9D6E2;
    --light-border: #DCE5EE;

}


/* ==========================================================
   ENTIRE APP
========================================================== */

html,
body,
[data-testid="stAppViewContainer"],
.stApp {

    background: var(--page-bg) !important;

    color: var(--text) !important;
}


/* ==========================================================
   REMOVE TOP STREAMLIT BAR
========================================================== */

header[data-testid="stHeader"] {

    background: transparent !important;
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


/* ==========================================================
   PAGE CONTAINER
========================================================== */

.block-container {

    padding-top: 1.4rem !important;
    padding-bottom: 3rem !important;

    max-width: 1200px;
}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {

    background: #FFFFFF !important;

    border-right:
        1px solid var(--light-border) !important;
}

section[data-testid="stSidebar"] > div {

    background: #FFFFFF !important;
}

section[data-testid="stSidebar"] * {

    color: var(--text);
}


/* ==========================================================
   TYPOGRAPHY
========================================================== */

h1 {

    color: var(--navy) !important;

    font-weight: 750 !important;

    letter-spacing: -0.5px;
}

h2,
h3 {

    color: var(--navy) !important;

    font-weight: 700 !important;
}

p {

    color: var(--muted);
}


/* ==========================================================
   SECTION LABELS
========================================================== */

.section-label {

    color: var(--bright-blue);

    font-size: 0.76rem;

    font-weight: 750;

    text-transform: uppercase;

    letter-spacing: 0.08em;

    margin-top: 12px;

    margin-bottom: 3px;
}


/* ==========================================================
   BADGE
========================================================== */

.prediction-badge {

    display: inline-block;

    background: #EAF5FD;

    color: var(--blue);

    border: 1px solid #CDE6FA;

    padding: 6px 14px;

    border-radius: 999px;

    font-size: 0.84rem;

    font-weight: 650;

    margin-bottom: 10px;
}


/* ==========================================================
   INTRO CARD
========================================================== */

.prediction-intro {

    background: #FFFFFF;

    border: 1px solid #D8E2EC;

    border-left: 5px solid var(--bright-blue);

    border-radius: 10px;

    padding: 20px 24px;

    margin-top: 12px;

    margin-bottom: 28px;

    box-shadow:
        0 5px 15px
        rgba(15, 47, 79, 0.07);
}

.prediction-intro p {

    color: var(--muted);

    line-height: 1.7;

    margin: 0;
}


/* ==========================================================
   WIDGET LABELS
========================================================== */

label,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {

    color: var(--muted) !important;

    font-weight: 600 !important;
}


/* ==========================================================
   SELECT BOX — COMPLETE LIGHT OVERRIDE
========================================================== */

/* Outer container */

[data-testid="stSelectbox"]
div[data-baseweb="select"] {

    background: transparent !important;
}


/* Actual selected-value box */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div {

    background-color: #FFFFFF !important;

    color: var(--text) !important;

    border:
        1px solid var(--border) !important;

    border-radius: 8px !important;

    min-height: 44px !important;

    box-shadow: none !important;
}


/* Every child inside select */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div * {

    color: var(--text) !important;

    background-color: transparent !important;

    -webkit-text-fill-color:
        var(--text) !important;
}


/* Selected text */

[data-testid="stSelectbox"]
span {

    color: var(--text) !important;

    -webkit-text-fill-color:
        var(--text) !important;
}


/* Arrow */

[data-testid="stSelectbox"] svg {

    fill: var(--muted) !important;

    color: var(--muted) !important;
}


/* Hover */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div:hover {

    border-color:
        #8CA9BE !important;
}


/* Focus */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div:focus-within {

    border-color:
        var(--bright-blue) !important;

    box-shadow:
        0 0 0 1px
        var(--bright-blue) !important;
}


/* ==========================================================
   DROPDOWN / POPOVER
========================================================== */

div[data-baseweb="popover"],
div[data-baseweb="menu"],
ul[role="listbox"] {

    background-color:
        #FFFFFF !important;

    color:
        var(--text) !important;
}


/* Individual options */

li[role="option"] {

    background-color:
        #FFFFFF !important;

    color:
        var(--text) !important;

    -webkit-text-fill-color:
        var(--text) !important;
}


/* Option text */

li[role="option"] * {

    color:
        var(--text) !important;

    -webkit-text-fill-color:
        var(--text) !important;
}


/* Option hover */

li[role="option"]:hover {

    background-color:
        #EAF5FD !important;

    color:
        var(--blue) !important;
}


/* Selected dropdown value */

li[aria-selected="true"] {

    background-color:
        #DCEFFD !important;

    color:
        var(--blue) !important;
}


/* ==========================================================
   TEXT INPUT
========================================================== */

[data-testid="stTextInput"]
div[data-baseweb="input"] {

    background-color:
        #FFFFFF !important;

    border:
        1px solid var(--border) !important;

    border-radius:
        8px !important;
}


[data-testid="stTextInput"] input {

    background-color:
        #FFFFFF !important;

    color:
        var(--text) !important;

    -webkit-text-fill-color:
        var(--text) !important;

    min-height:
        44px !important;

    border:
        none !important;
}


[data-testid="stTextInput"]
div[data-baseweb="input"]:focus-within {

    border-color:
        var(--bright-blue) !important;

    box-shadow:
        0 0 0 1px
        var(--bright-blue) !important;
}


/* ==========================================================
   NUMBER INPUT
========================================================== */

[data-testid="stNumberInput"]
div[data-baseweb="input"] {

    background-color:
        #FFFFFF !important;

    border:
        1px solid var(--border) !important;

    border-radius:
        8px !important;

    overflow:
        hidden !important;
}


[data-testid="stNumberInput"] input {

    background-color:
        #FFFFFF !important;

    color:
        var(--text) !important;

    -webkit-text-fill-color:
        var(--text) !important;

    border:
        none !important;

    min-height:
        44px !important;
}


/* Increment/decrement buttons */

[data-testid="stNumberInput"] button {

    background-color:
        var(--blue) !important;

    color:
        #FFFFFF !important;

    border:
        none !important;
}


[data-testid="stNumberInput"] button:hover {

    background-color:
        var(--blue-hover) !important;
}


/* Plus/minus icons */

[data-testid="stNumberInput"] button svg {

    color:
        #FFFFFF !important;

    fill:
        #FFFFFF !important;
}


/* ==========================================================
   DIVIDERS
========================================================== */

hr {

    border-color:
        var(--light-border) !important;

    margin-top:
        1.8rem !important;

    margin-bottom:
        1.8rem !important;
}


/* ==========================================================
   PREDICTION BUTTON
========================================================== */

[data-testid="stButton"] > button,
div.stButton > button {

    background:
        var(--blue) !important;

    border:
        1px solid var(--blue) !important;

    border-radius:
        8px !important;

    min-height:
        52px !important;

    width:
        100% !important;

    box-shadow:
        0 4px 12px
        rgba(20, 91, 143, 0.20);

    transition:
        all 0.2s ease;
}


/* Force ALL button text white */

[data-testid="stButton"] > button *,
div.stButton > button *,
[data-testid="stButton"] > button,
div.stButton > button {

    color:
        #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    font-weight:
        700 !important;
}


/* Hover */

[data-testid="stButton"] > button:hover,
div.stButton > button:hover {

    background:
        var(--blue-hover) !important;

    border-color:
        var(--blue-hover) !important;

    transform:
        translateY(-1px);

    box-shadow:
        0 6px 16px
        rgba(20, 91, 143, 0.28);
}


/* ==========================================================
   METRIC CARDS
========================================================== */

[data-testid="stMetric"] {

    background:
        #FFFFFF !important;

    border:
        1px solid #D8E2EC;

    border-radius:
        10px;

    padding:
        20px 22px;

    min-height:
        120px;

    box-shadow:
        0 5px 14px
        rgba(15, 47, 79, 0.08);
}


[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] * {

    color:
        var(--muted) !important;
}


[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {

    color:
        var(--blue) !important;

    font-weight:
        750 !important;
}


/* ==========================================================
   HIGH RISK
========================================================== */

.high-risk-box {

    background:
        #FFF1F2;

    border:
        1px solid #F5C2C7;

    border-left:
        5px solid #D94452;

    color:
        #9F1D2B;

    padding:
        16px 18px;

    border-radius:
        8px;

    font-weight:
        650;

    margin:
        15px 0 20px;
}


/* ==========================================================
   MEDIUM RISK
========================================================== */

.medium-risk-box {

    background:
        #FFF7E6;

    border:
        1px solid #F7D89A;

    border-left:
        5px solid #F59E0B;

    color:
        #92400E;

    padding:
        16px 18px;

    border-radius:
        8px;

    font-weight:
        650;

    margin:
        15px 0 20px;
}


/* ==========================================================
   LOW RISK
========================================================== */

.low-risk-box {

    background:
        #ECFDF5;

    border:
        1px solid #B7E8D2;

    border-left:
        5px solid #10B981;

    color:
        #066045;

    padding:
        16px 18px;

    border-radius:
        8px;

    font-weight:
        650;

    margin:
        15px 0 20px;
}


/* ==========================================================
   RECOMMENDATION CARD
========================================================== */

.recommendation-box {

    background:
        #EDF6FD;

    border:
        1px solid #CDE4F5;

    border-left:
        5px solid var(--blue);

    color:
        var(--text);

    padding:
        18px 20px;

    border-radius:
        8px;

    margin:
        8px 0 22px;

    box-shadow:
        0 3px 10px
        rgba(15, 47, 79, 0.05);
}


/* ==========================================================
   DATAFRAME
========================================================== */

[data-testid="stDataFrame"] {

    background:
        #FFFFFF !important;

    border:
        1px solid #D8E2EC;

    border-radius:
        10px;

    overflow:
        hidden;

    box-shadow:
        0 4px 12px
        rgba(15, 47, 79, 0.07);
}


/* ==========================================================
   FOOTER
========================================================== */

.footer-text {

    text-align:
        center;

    color:
        #8797A8;

    font-size:
        0.82rem;

    margin-top:
        25px;
}

</style>
""",
    unsafe_allow_html=True
)


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
<strong>Logistic Regression model</strong>.
Enter customer demographic, account and service information
to estimate churn risk and generate a targeted
retention recommendation.
</p>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.markdown(
    '<div class="section-label">Customer Profile</div>',
    unsafe_allow_html=True
)

st.subheader(
    "👤 Customer Information"
)

col1, col2, col3 = st.columns(3)


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
            "Latitude": [latitude],
            "Longitude": [longitude],

            "Country": [country],
            "State": [state],

            "Gender": [gender],
            "Senior Citizen": [senior_citizen],
            "Partner": [partner],
            "Dependents": [dependents],

            "Tenure Months": [tenure],

            "Phone Service": [phone_service],
            "Multiple Lines": [multiple_lines],

            "Internet Service": [internet_service],

            "Online Security": [online_security],
            "Online Backup": [online_backup],
            "Device Protection": [device_protection],
            "Tech Support": [tech_support],

            "Streaming TV": [streaming_tv],
            "Streaming Movies": [streaming_movies],

            "Contract": [contract],
            "Paperless Billing": [paperless_billing],
            "Payment Method": [payment_method],

            "Monthly Charges": [monthly_charges],
            "Total Charges": [total_charges],

            "CLTV": [cltv]
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
    # THRESHOLD
    # ========================================================

    prediction = int(
        churn_probability
        >= threshold
    )

    probability_percent = (
        churn_probability * 100
    )


    # ========================================================
    # RESULT
    # ========================================================

    st.divider()

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
🔴 High Risk — Immediate retention action recommended.
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
🟠 Medium Risk — Customer should be monitored closely.
</div>
""",
            unsafe_allow_html=True
        )


    else:

        risk_level = "Low Risk"

        recommendation = "Monitor"

        st.markdown(
            """
<div class="low-risk-box">
🟢 Low Risk — No immediate retention action required.
</div>
""",
            unsafe_allow_html=True
        )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.subheader(
        "💡 Recommended Action"
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
        "📋 Customer Summary"
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
Python
&nbsp; • &nbsp;
Streamlit
&nbsp; • &nbsp;
Logistic Regression
&nbsp; • &nbsp;
Predictive Analytics
</div>
""",
    unsafe_allow_html=True
)
