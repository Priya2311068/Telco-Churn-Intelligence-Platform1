import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# Current file:
# project_root/pages/2_🤖_Churn_Prediction.py
#
# parents[1] takes us back to the GitHub project root.
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

    # Make sure threshold is a normal float
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
# TITLE
# ============================================================

st.title(
    "🎯 Telco Customer Churn Prediction"
)

st.markdown(
    """
    Predict customer churn risk using the trained
    **Logistic Regression model**.
    """
)

st.divider()


# ============================================================
# CUSTOMER INPUT
# ============================================================

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
    "🔮 Predict Churn Risk",
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
        churn_probability
        >= threshold
    )

    probability_percent = (
        churn_probability
        * 100
    )


    st.divider()


    # ========================================================
    # RESULT
    # ========================================================

    st.subheader(
        "🎯 Prediction Result"
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

        st.error(
            "🔴 High Risk — Immediate retention "
            "action recommended."
        )


    elif probability_percent >= 40:

        risk_level = "Medium Risk"

        recommendation = (
            "Targeted retention campaign and "
            "monitor customer behavior"
        )

        st.warning(
            "🟠 Medium Risk — Customer should "
            "be monitored."
        )


    else:

        risk_level = "Low Risk"

        recommendation = (
            "Monitor"
        )

        st.success(
            "🟢 Low Risk — No immediate "
            "action required."
        )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.subheader(
        "💡 Recommended Action"
    )

    st.info(
        recommendation
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
