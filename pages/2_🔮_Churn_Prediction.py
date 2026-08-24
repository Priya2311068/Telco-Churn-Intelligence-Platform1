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
# COLOR SYSTEM
# ============================================================

BG = "#EDF4F7"

CARD = "#FFFFFF"

BORDER = "#D5E1E7"

TEXT = "#0F2942"

MUTED = "#64748B"

BLUE = "#1697A6"

NAVY = "#147F8B"

PURPLE = "#1697A6"

CORAL = "#E6535F"

GREEN = "#2A9D8F"


# ============================================================
# COMPLETE LIGHT THEME
# ============================================================

st.markdown(
    f"""
<style>


/* ==========================================================
   FORCE LIGHT COLOR SCHEME
========================================================== */

:root {{

    color-scheme: light !important;

}}


html,
body,
[data-testid="stAppViewContainer"],
.stApp {{

    color-scheme: light !important;

    background: {BG} !important;

    color: {TEXT} !important;

}}


/* ==========================================================
   MAIN APPLICATION
========================================================== */

.stApp {{

    background-color: {BG} !important;

    color: {TEXT} !important;

}}


.block-container {{

    max-width: 1200px;

    padding-top: 1.2rem !important;

    padding-bottom: 3rem !important;

}}


/* ==========================================================
   STREAMLIT TOP HEADER
========================================================== */

header[data-testid="stHeader"] {{

    background: transparent !important;

}}


div[data-testid="stToolbar"] {{

    visibility: hidden !important;

    height: 0 !important;

}}


div[data-testid="stDecoration"] {{

    display: none !important;

}}


div[data-testid="stStatusWidget"] {{

    visibility: hidden !important;

}}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    border-right: 1px solid {BORDER} !important;

}}


section[data-testid="stSidebar"] > div {{

    background: #FFFFFF !important;

}}


section[data-testid="stSidebar"] * {{

    color: {TEXT};

}}


/* ==========================================================
   PAGE TITLES
========================================================== */

h1 {{

    color: #0F2942 !important;

    font-weight: 750 !important;

    letter-spacing: -0.5px;

}}


h2,
h3 {{

    color: #0F2942 !important;

    font-weight: 700 !important;

}}


p {{

    color: {MUTED};

}}


/* ==========================================================
   SMALL SECTION LABELS
========================================================== */

.section-label {{

    color: {BLUE};

    font-size: 0.76rem;

    font-weight: 750;

    text-transform: uppercase;

    letter-spacing: 0.08em;

    margin-top: 12px;

    margin-bottom: 3px;

}}


/* ==========================================================
   PAGE BADGE
========================================================== */

.prediction-badge {{

    display: inline-block;

    background: #E7F5F6;

    color: {NAVY};

    border: 1px solid #BFE3E7;

    padding: 6px 14px;

    border-radius: 999px;

    font-size: 0.84rem;

    font-weight: 650;

    margin-bottom: 8px;

}}


/* ==========================================================
   INTRO CARD
========================================================== */

.prediction-intro {{

    background: #FFFFFF;

    border: 1px solid #D8E2EC;

    border-left: 5px solid {BLUE};

    border-radius: 10px;

    padding: 20px 24px;

    margin-top: 10px;

    margin-bottom: 28px;

    box-shadow:
        0 5px 15px
        rgba(15,47,79,.07);

}}


.prediction-intro p {{

    color: {MUTED};

    margin: 0;

    line-height: 1.7;

}}


/* ==========================================================
   FORM LABELS
========================================================== */

label,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {{

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

    font-weight: 600 !important;

}}


/* ==========================================================
   TEXT INPUTS
========================================================== */

[data-testid="stTextInput"]
div[data-baseweb="input"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    border: 1px solid #B8C7D9 !important;

    border-radius: 8px !important;

}}


[data-testid="stTextInput"] input {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

    min-height: 44px !important;

    border: none !important;

}}


[data-testid="stTextInput"]
div[data-baseweb="input"]:focus-within {{

    border-color: {BLUE} !important;

    box-shadow:
        0 0 0 1px
        {BLUE} !important;

}}


/* ==========================================================
   NUMBER INPUT
========================================================== */

[data-testid="stNumberInput"]
div[data-baseweb="input"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    border: 1px solid #B8C7D9 !important;

    border-radius: 8px !important;

    overflow: hidden !important;

}}


[data-testid="stNumberInput"] input {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

    border: none !important;

    min-height: 44px !important;

}}


/* NUMBER +/- BUTTONS */

[data-testid="stNumberInput"] button {{

    background: {NAVY} !important;

    color: #FFFFFF !important;

    border: none !important;

}}


[data-testid="stNumberInput"] button:hover {{

    background: #106C76 !important;

}}


[data-testid="stNumberInput"] button svg {{

    color: #FFFFFF !important;

    fill: #FFFFFF !important;

}}


/* ==========================================================
   SELECTBOXES
   THIS FIXES THE DARK FIELDS IN YOUR SCREENSHOT
========================================================== */

[data-testid="stSelectbox"] {{

    color-scheme: light !important;

    background: transparent !important;

}}


[data-testid="stSelectbox"]
div[data-baseweb="select"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

}}


/* Main visible dropdown */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

    color: {TEXT} !important;

    border: 1px solid #B8C7D9 !important;

    border-radius: 8px !important;

    min-height: 44px !important;

    box-shadow: none !important;

}}


/* Inner Streamlit/BaseWeb layers */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div > div {{

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

}}


[data-testid="stSelectbox"]
div[data-baseweb="select"] > div > div > div {{

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

}}


/* Actual combobox */

[data-testid="stSelectbox"]
[role="combobox"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

}}


/* Additional Streamlit fallback */

[data-testid="stSelectbox"]
[aria-haspopup="listbox"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

}}


/* Selected text */

[data-testid="stSelectbox"] span,

[data-testid="stSelectbox"] p {{

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

}}


/* Dropdown arrow */

[data-testid="stSelectbox"] svg {{

    color: {MUTED} !important;

    fill: {MUTED} !important;

}}


/* Hover */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div:hover {{

    background: #FFFFFF !important;

    border-color: #94B4CE !important;

}}


/* Focus */

[data-testid="stSelectbox"]
div[data-baseweb="select"] > div:focus-within {{

    background: #FFFFFF !important;

    border-color: {BLUE} !important;

    box-shadow:
        0 0 0 1px
        {BLUE} !important;

}}


/* ==========================================================
   OPEN DROPDOWN MENU
========================================================== */

div[data-baseweb="popover"],

div[data-baseweb="menu"],

ul[role="listbox"] {{

    color-scheme: light !important;

    background: #FFFFFF !important;

    background-color: #FFFFFF !important;

    color: {TEXT} !important;

}}


ul[role="listbox"] {{

    border: 1px solid {BORDER} !important;

    border-radius: 8px !important;

    box-shadow:
        0 6px 18px
        rgba(22,50,79,.12) !important;

}}


/* DROPDOWN OPTIONS */

li[role="option"] {{

    background: #FFFFFF !important;

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

}}


li[role="option"] * {{

    color: {TEXT} !important;

    -webkit-text-fill-color:
        {TEXT} !important;

}}


li[role="option"]:hover {{

    background: #EAF7F8 !important;

    color: {NAVY} !important;

    -webkit-text-fill-color:
        {NAVY} !important;

}}


li[role="option"][aria-selected="true"] {{

    background: #D8F0F2 !important;

    color: {NAVY} !important;

    -webkit-text-fill-color:
        {NAVY} !important;

}}


/* ==========================================================
   LIGHT DROPDOWN SCROLLBARS
========================================================== */

ul[role="listbox"]::-webkit-scrollbar {{

    width: 7px !important;

}}


ul[role="listbox"]::-webkit-scrollbar-track {{

    background: #F1F5F9 !important;

    border-radius: 8px;

}}


ul[role="listbox"]::-webkit-scrollbar-thumb {{

    background: #B8C7D9 !important;

    border-radius: 10px;

}}


ul[role="listbox"]::-webkit-scrollbar-thumb:hover {{

    background: #94A8BD !important;

}}


/* ==========================================================
   PAGE SCROLLBAR
========================================================== */

html::-webkit-scrollbar,
body::-webkit-scrollbar,
.stApp::-webkit-scrollbar,
[data-testid="stAppViewContainer"]::-webkit-scrollbar {{

    width: 9px !important;

}}


html::-webkit-scrollbar-track,
body::-webkit-scrollbar-track,
.stApp::-webkit-scrollbar-track,
[data-testid="stAppViewContainer"]::-webkit-scrollbar-track {{

    background: #F1F5F9 !important;

}}


html::-webkit-scrollbar-thumb,
body::-webkit-scrollbar-thumb,
.stApp::-webkit-scrollbar-thumb,
[data-testid="stAppViewContainer"]::-webkit-scrollbar-thumb {{

    background: #C2CFDC !important;

    border-radius: 10px !important;

}}


html::-webkit-scrollbar-thumb:hover,
body::-webkit-scrollbar-thumb:hover,
.stApp::-webkit-scrollbar-thumb:hover,
[data-testid="stAppViewContainer"]::-webkit-scrollbar-thumb:hover {{

    background: #9FB1C3 !important;

}}


/* ==========================================================
   STREAMLIT INTERNAL SCROLLABLE AREAS
========================================================== */

[data-testid="stSidebar"] ::-webkit-scrollbar,
[data-testid="stVerticalBlock"] ::-webkit-scrollbar {{

    width: 7px !important;

    height: 7px !important;

}}


[data-testid="stSidebar"] ::-webkit-scrollbar-track,
[data-testid="stVerticalBlock"] ::-webkit-scrollbar-track {{

    background: #F1F5F9 !important;

}}


[data-testid="stSidebar"] ::-webkit-scrollbar-thumb,
[data-testid="stVerticalBlock"] ::-webkit-scrollbar-thumb {{

    background: #BCCBDA !important;

    border-radius: 10px !important;

}}


/* ==========================================================
   DIVIDERS
========================================================== */

hr {{

    border-color: #DCE5EE !important;

    margin-top: 1.8rem !important;

    margin-bottom: 1.8rem !important;

}}


/* ==========================================================
   PREDICTION BUTTON
========================================================== */

[data-testid="stButton"] > button,
div.stButton > button {{

    width: 100% !important;

    min-height: 52px !important;

    background: {NAVY} !important;

    border: 1px solid {NAVY} !important;

    border-radius: 8px !important;

    box-shadow:
        0 4px 12px
        rgba(20,127,139,.20);

    transition:
        all .2s ease;

}}


/* WHITE BUTTON TEXT */

[data-testid="stButton"] > button,
[data-testid="stButton"] > button *,
div.stButton > button,
div.stButton > button * {{

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    font-weight: 700 !important;

}}


[data-testid="stButton"] > button:hover,
div.stButton > button:hover {{

    background: #106C76 !important;

    border-color: #106C76 !important;

    transform: translateY(-1px);

    box-shadow:
        0 6px 16px
        rgba(20,127,139,.28);

}}


/* ==========================================================
   METRIC CARDS
========================================================== */

[data-testid="stMetric"] {{

    background: #FFFFFF !important;

    border: 1px solid #D8E2EC;

    border-radius: 10px;

    padding: 20px 22px;

    min-height: 120px;

    box-shadow:
        0 5px 14px
        rgba(15,47,79,.08);

}}


[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] * {{

    color: {MUTED} !important;

}}


[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {{

    color: {NAVY} !important;

    font-weight: 750 !important;

}}


/* ==========================================================
   HIGH RISK
========================================================== */

.high-risk-box {{

    background: #FFF1F2;

    border: 1px solid #F5C2C7;

    border-left: 5px solid {CORAL};

    color: #9F1D2B;

    padding: 16px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin: 15px 0 20px;

}}


/* ==========================================================
   MEDIUM RISK
========================================================== */

.medium-risk-box {{

    background: #FFF7E6;

    border: 1px solid #F7D89A;

    border-left: 5px solid #F59E0B;

    color: #92400E;

    padding: 16px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin: 15px 0 20px;

}}


/* ==========================================================
   LOW RISK
========================================================== */

.low-risk-box {{

    background: #ECFDF5;

    border: 1px solid #B7E8D2;

    border-left: 5px solid {GREEN};

    color: #066045;

    padding: 16px 18px;

    border-radius: 8px;

    font-weight: 650;

    margin: 15px 0 20px;

}}


/* ==========================================================
   RECOMMENDATION
========================================================== */

.recommendation-box {{

    background: #F2F9FA;

    border: 1px solid #C7E3E6;

    border-left: 5px solid {BLUE};

    color: {TEXT};

    padding: 18px 20px;

    border-radius: 8px;

    margin: 8px 0 22px;

    box-shadow:
        0 3px 10px
        rgba(15,47,79,.05);

}}


/* ==========================================================
   DATAFRAME
========================================================== */

[data-testid="stDataFrame"] {{

    background: #FFFFFF !important;

    border: 1px solid #D8E2EC;

    border-radius: 10px;

    overflow: hidden;

    box-shadow:
        0 4px 12px
        rgba(15,47,79,.07);

}}


/* ==========================================================
   FOOTER
========================================================== */

.footer-text {{

    text-align: center;

    color: #8797A8;

    font-size: .82rem;

    margin-top: 25px;

}}


/* ==========================================================
   REMOVE STREAMLIT DEFAULT ITEMS
========================================================== */

#MainMenu {{

    visibility: hidden;

}}


footer {{

    visibility: hidden;

}}


/* ==========================================================
   PROFESSIONAL CUSTOMER SUMMARY TABLE
========================================================== */

.summary-table-wrap {{
    background: #FFFFFF;
    border: 1px solid #D5E1E7;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(15,47,79,.07);
    margin-top: 6px;
    margin-bottom: 8px;
}}

.summary-table {{
    width: 100%;
    border-collapse: collapse;
    background: #FFFFFF;
    color: #0F2942;
    font-size: 0.96rem;
}}

.summary-table thead th {{
    background: #E7F5F6;
    color: #147F8B;
    text-align: left;
    padding: 12px 14px;
    font-weight: 750;
    border-bottom: 1px solid #D5E1E7;
}}

.summary-table tbody td {{
    background: #FFFFFF;
    color: #0F2942;
    padding: 11px 14px;
    border-bottom: 1px solid #E6EDF2;
}}

.summary-table tbody tr:last-child td {{
    border-bottom: none;
}}

.summary-table tbody tr:hover td {{
    background: #F5FAFB;
}}

.summary-table tbody td:first-child {{
    width: 42%;
    font-weight: 650;
    color: #334E68;
}}

/* Slightly more polished section headings */
h2, h3 {{
    letter-spacing: -0.25px;
}}

/* Keep risk red only where it communicates churn/high risk */
.high-risk-box {{
    box-shadow: 0 3px 10px rgba(230,83,95,.08);
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# PAGE TITLE
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
to estimate churn risk and generate a targeted retention
recommendation.

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
    # THRESHOLD
    # ========================================================

    prediction = int(
        churn_probability
        >= threshold
    )


    probability_percent = (
        churn_probability
        * 100
    )


    # ========================================================
    # RESULTS
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

        risk_level = (
            "High Risk"
        )


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

        risk_level = (
            "Medium Risk"
        )


        recommendation = (
            "Targeted retention campaign "
            "and monitor customer behavior"
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

        risk_level = (
            "Low Risk"
        )


        recommendation = (
            "Monitor"
        )


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

<strong>
{recommendation}
</strong>

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


    summary[
        "Value"
    ] = (
        summary[
            "Value"
        ]
        .astype(str)
    )


    # Render as HTML instead of st.dataframe so the summary remains
    # consistently light even when the browser/Streamlit theme is dark.
    summary_rows = "".join(
        f"<tr><td>{feature}</td><td>{value}</td></tr>"
        for feature, value in zip(summary["Feature"], summary["Value"])
    )

    st.markdown(
        f"""
        <div class="summary-table-wrap">
            <table class="summary-table">
                <thead>
                    <tr>
                        <th>Feature</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {summary_rows}
                </tbody>
            </table>
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
Logistic Regression
&nbsp; • &nbsp;
Predictive Analytics

</div>
""",
    unsafe_allow_html=True
)
