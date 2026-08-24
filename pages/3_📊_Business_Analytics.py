import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path
from textwrap import dedent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Telco Customer Churn Analytics",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# THEME
# ============================================================

# Overall page background is intentionally darker than chart/cards
# to create stronger visual separation without using a dark theme.
BG = "#E9EFF5"

# Clean visual/chart surfaces
CARD = "#FFFFFF"
CARD_2 = "#F4F7FA"

# Slightly darker plotting area inside white chart cards
PLOT_BG = "#F6F8FB"

BORDER = "#D3DEE8"

# Main analytical palette
CYAN = "#168CE3"      # Primary analytics
TEAL = "#145B8F"      # Deep blue accent
PURPLE = "#6D28D9"    # Recommendation/accent only
ORANGE = "#E0525E"    # Churn / risk
GREEN = "#2A9D8F"     # Positive / retained

TEXT = "#16324F"
MUTED = "#64748B"


# ============================================================
# CONSISTENT VISUAL FONT SIZES
# ============================================================

DATA_LABEL_SIZE = 13
AXIS_LABEL_SIZE = 10.5
AXIS_TITLE_SIZE = 11
CHART_TITLE_SIZE = 14
CATEGORY_LABEL_SIZE = 11


# ============================================================
# HTML HELPER
# ============================================================

def html(content):
    st.html(dedent(content).strip())


# ============================================================
# GLOBAL CSS
# ============================================================

html(
    f"""
    <style>

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1600px !important;
        padding-top: 0.25rem !important;
        padding-bottom: 0.25rem !important;
        padding-left: 0.55rem !important;
        padding-right: 0.55rem !important;
    }}

    header[data-testid="stHeader"] {{
        height: 27px;
        background: transparent;
    }}


    /* ======================================================
       HEADER
    ====================================================== */

    .hero {{
        background:
            linear-gradient(
                120deg,
                #FFFFFF,
                #F5F9FD
            );

        border: 1px solid {BORDER};
        border-radius: 13px;

        height: 61px;
        box-sizing: border-box;

        padding: 8px 14px;

        display: flex;
        align-items: center;

        margin-bottom: 4px;

        box-shadow:
            0 4px 12px rgba(15,47,79,.05);
    }}

    .hero-icon {{
        height: 38px;
        width: 38px;

        border-radius: 10px;

        display: flex;
        justify-content: center;
        align-items: center;

        font-size: 19px;

        background:
            linear-gradient(
                135deg,
                rgba(22,140,227,.14),
                rgba(109,40,217,.10)
            );

        margin-right: 11px;
    }}

    .hero-title {{
        font-size: 23px;
        font-weight: 850;
        line-height: 1;
        color: {TEXT};
    }}

    .hero-subtitle {{
        font-size: 8.4px;
        letter-spacing: .9px;
        color: {MUTED};
        margin-top: 5px;
        font-weight: 600;
    }}


    /* ======================================================
       SECTION TITLE
    ====================================================== */

    .section-title {{
        color: {TEXT};
        font-size: 13.5px;
        font-weight: 850;
        margin-top: 4px;
        margin-bottom: 4px;
    }}

    .row-gap {{
        height: 10px;
    }}


    /* ======================================================
       KPI
    ====================================================== */

    .kpi {{
        height: 82px;
        box-sizing: border-box;

        padding: 8px 10px;

        border-radius: 11px;
        border: 1px solid {BORDER};

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

        box-shadow:
            0 5px 14px rgba(15,47,79,.08);
    }}

    .kpi-icon {{
        width: 24px;
        height: 24px;

        border-radius: 7px;

        display: flex;
        justify-content: center;
        align-items: center;

        font-size: 13px;

        background:
            linear-gradient(
                135deg,
                rgba(22,140,227,.18),
                rgba(109,40,217,.12)
            );
    }}

    .kpi-value {{
        font-size: 18.5px;
        font-weight: 850;
        color: {TEXT};
        margin-top: 5px;
        line-height: 1;
    }}

    .kpi-label {{
        font-size: 9px;
        color: {MUTED};
        margin-top: 5px;
        font-weight: 600;
    }}


    /* ======================================================
       RECOMMENDATIONS
    ====================================================== */

    .recommend {{
        min-height: 70px;
        box-sizing: border-box;

        border: 1px solid {BORDER};
        border-radius: 10px;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

        box-shadow:
            0 4px 12px rgba(15,47,79,.07);

        padding: 10px 11px;
    }}

    .recommend-title {{
        color: {PURPLE};
        font-size: 13.7px;
        font-weight: 850;
    }}

    .recommend-text {{
        color: {TEXT};
        font-size: 11.7px;
        line-height: 1.38;
        margin-top: 4px;
    }}


    /* ======================================================
       PLOTLY CARDS
    ====================================================== */

    div[data-testid="stPlotlyChart"] {{
        border: 1px solid {BORDER};
        border-radius: 11px;

        background: {CARD};

        overflow: hidden;

        box-shadow:
            0px 4px 12px rgba(15,47,79,.08);
    }}


    /* ======================================================
       SPACING
    ====================================================== */

    div[data-testid="stVerticalBlock"] {{
        gap: 0.20rem !important;
    }}

    div[data-testid="stHorizontalBlock"] {{
        gap: 0.65rem !important;
    }}

    div[data-testid="column"] {{
        padding-left: 0px !important;
        padding-right: 0px !important;
    }}


    /* ======================================================
       SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {{
        color-scheme: light !important;
        background: #FFFFFF;

        border-right: 1px solid {BORDER};
    }}

    div[data-baseweb="select"] > div {{
        background: #FFFFFF;
        color: {TEXT};
        border: 1px solid {BORDER};
        min-height: 34px;
        border-radius: 8px;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}


    /* ======================================================
       LIGHT THEME CONSISTENCY
    ====================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"] {{
        background: {BG} !important;
        color: {TEXT} !important;
        color-scheme: light !important;
    }}

    section[data-testid="stSidebar"] * {{
        color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div,
    div[data-baseweb="select"] > div {{
        background: #FFFFFF !important;
        color: {TEXT} !important;
        border: 1px solid #C9D6E2 !important;
    }}

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] svg {{
        color: {TEXT} !important;
        fill: {MUTED} !important;
    }}

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"],
    li[role="option"] {{
        background: #FFFFFF !important;
        color: {TEXT} !important;
    }}

    li[role="option"]:hover {{
        background: #EAF5FD !important;
        color: {TEAL} !important;
    }}

    .hero,
    .kpi,
    .recommend,
    div[data-testid="stPlotlyChart"] {{
        color: {TEXT} !important;
    }}

    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}


    /* ======================================================
       SIDEBAR FILTERS
    ====================================================== */

    section[data-testid="stSidebar"] {{
        background: #FFFFFF !important;
        border-right: 1px solid {BORDER} !important;
    }}

    section[data-testid="stSidebar"] > div {{
        background: #FFFFFF !important;
    }}

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    div[data-baseweb="select"] > div {{
        color-scheme: light !important;
        background: #FFFFFF !important;
        color: {TEXT} !important;
        border: 1px solid #C9D6E2 !important;
        border-radius: 8px !important;
        min-height: 42px !important;
        box-shadow:
            0 2px 6px rgba(15,47,79,.04) !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    div[data-baseweb="select"] > div * {{
        background: transparent !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"] svg {{
        color: {MUTED} !important;
        fill: {MUTED} !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    [role="combobox"],
    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    [aria-haspopup="listbox"] {{
        color-scheme: light !important;
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    [role="combobox"] *,
    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    [aria-haspopup="listbox"] * {{
        background: transparent !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    div[data-baseweb="select"] > div:hover {{
        border-color: #94B4CE !important;
    }}

    section[data-testid="stSidebar"]
    [data-testid="stSelectbox"]
    div[data-baseweb="select"] > div:focus-within {{
        border-color: {CYAN} !important;
        box-shadow:
            0 0 0 1px {CYAN} !important;
    }}

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {{
        color-scheme: light !important;
        background: #FFFFFF !important;
        color: {TEXT} !important;
        border-color: {BORDER} !important;
    }}

    li[role="option"] {{
        background: #FFFFFF !important;
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    li[role="option"] * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    li[role="option"]:hover {{
        background: #EAF5FD !important;
        color: {TEAL} !important;
        -webkit-text-fill-color: {TEAL} !important;
    }}

    li[role="option"][aria-selected="true"] {{
        background: #DCEFFD !important;
        color: {TEAL} !important;
        -webkit-text-fill-color: {TEAL} !important;
    }}

    </style>
    """
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    possible_paths = [
        Path("telco_customer_churn.csv"),
        Path("Telco_Churn_Project/telco_customer_churn.csv"),
        Path("data/telco_customer_churn.csv"),
    ]

    for path in possible_paths:

        if path.exists():
            return pd.read_csv(path)

    return None


df = load_data()


if df is None:
    st.error("Could not find telco_customer_churn.csv")
    st.stop()


df.columns = df.columns.str.strip()


# ============================================================
# COLUMN FINDER
# ============================================================

def find_column(names):

    normalized = {
        col.lower()
        .replace("_", "")
        .replace(" ", ""): col
        for col in df.columns
    }

    for name in names:

        key = (
            name.lower()
            .replace("_", "")
            .replace(" ", "")
        )

        if key in normalized:
            return normalized[key]

    return None


churn_col = find_column([
    "Churn",
    "Churn Label",
    "Churn Value",
    "Customer Status"
])

tenure_col = find_column([
    "Tenure",
    "tenure",
    "Tenure Months"
])

monthly_col = find_column([
    "MonthlyCharges",
    "Monthly Charges"
])

total_col = find_column([
   
