import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path
from textwrap import dedent
import html as html_lib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="High Risk Customer Retention Center",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# COLORS
# ============================================================

BG = "#E7EFF4"
CARD = "#FFFFFF"
CARD_2 = "#F4F8FA"
BORDER = "#D3E0E7"

CYAN = "#1697A6"
TEAL = "#1697A6"
PURPLE = "#1697A6"
ORANGE = "#1697A6"
RED = "#E6535D"
GREEN = "#1697A6"

TEXT = "#102A43"
MUTED = "#486581"


# ============================================================
# DASHBOARD SETTINGS
# ============================================================

KPI_HEIGHT = 68
CHART_HEIGHT = 158

CHART_TITLE_SIZE = 14.5

# Consistent readable labels across ALL bar charts
DATA_LABEL_SIZE = 13
CATEGORY_LABEL_SIZE = 11.5
AXIS_TITLE_SIZE = 12

WATCHLIST_HEIGHT = 220
ROW_GAP = 5


# ============================================================
# HTML HELPER
# ============================================================

def html(content):
    st.html(dedent(content).strip())


# ============================================================
# CSS
# ============================================================

html(
    f"""
    <style>

    .stApp {{
        background:
            radial-gradient(
                circle at 10% 0%,
                #F1F6F9 0%,
                {BG} 32%,
                #DDE8EE 100%
            );
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1650px !important;
        padding-top: 0.02rem !important;
        padding-bottom: 0.02rem !important;
        padding-left: 0.45rem !important;
        padding-right: 0.45rem !important;
    }}

    header[data-testid="stHeader"] {{
        height: 18px !important;
        min-height: 18px !important;
        background: transparent !important;
    }}

    .hero {{
        height: 50px;
        box-sizing: border-box;
        padding: 5px 12px;
        display: flex;
        align-items: center;
        border: 1px solid {BORDER};
        border-radius: 11px;
        background:
            linear-gradient(
                120deg,
                #FFFFFF,
                #F4F8FA
            );
        margin-bottom: 3px;
    }}

    .hero-icon {{
        width: 33px;
        height: 33px;
        min-width: 33px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        border-radius: 9px;
        font-size: 18px;
        background:
            linear-gradient(
                135deg,
                rgba(22,151,166,.14),
                rgba(230,83,93,.12)
            );
    }}

    .hero-title {{
        font-size: 21px;
        font-weight: 850;
        line-height: 1;
        color: {TEXT};
    }}

    .hero-subtitle {{
        margin-top: 4px;
        font-size: 7.4px;
        letter-spacing: .65px;
        color: {MUTED};
    }}

    .section-title {{
        margin-top: 5px;
        margin-bottom: 5px;
        font-size: 12.5px;
        font-weight: 850;
        line-height: 1;
        color: {TEXT};
    }}

    .row-gap {{
        height: {ROW_GAP}px;
    }}

    .kpi {{
        height: {KPI_HEIGHT}px;
        box-sizing: border-box;
        padding: 7px 11px;
        border: 1px solid {BORDER};
        border-radius: 10px;
        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F6F9FB
            );
    }}

    .kpi-top {{
        display: flex;
        align-items: center;
        gap: 9px;
    }}

    .kpi-icon {{
        width: 25px;
        height: 25px;
        min-width: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 7px;
        font-size: 13px;
        background:
            linear-gradient(
                135deg,
                rgba(22,151,166,.13),
                rgba(22,151,166,.09)
            );
    }}

    .kpi-value {{
        font-size: 21px;
        font-weight: 850;
        line-height: 1;
        color: {TEXT};
    }}

    .kpi-label {{
        margin-top: 6px;
        font-size: 9.4px;
        font-weight: 500;
        color: {MUTED};
    }}

    div[data-testid="stPlotlyChart"] {{
        border: 1px solid {BORDER};
        border-radius: 10px;
        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F7FAFC
            );
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(16,42,67,.07);
    }}

    .watch-title {{
        margin-top: 3px;
        margin-bottom: 4px;
        font-size: 12px;
        font-weight: 850;
        color: {TEXT};
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {BORDER};
        border-radius: 10px;
        overflow: hidden;
        background: #FFFFFF;
    }}

    div[data-testid="stVerticalBlock"] {{
        gap: 0.03rem !important;
    }}

    div[data-testid="stHorizontalBlock"] {{
        gap: 0.62rem !important;
    }}

    div[data-testid="column"] {{
        padding-left: 0 !important;
        padding-right: 0 !important;
    }}

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                #F8FBFD,
                #EEF4F7
            );
        border-right: 1px solid {BORDER};
    }}

    /* Force all sidebar/navigation content to remain readable on light background */
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] div {{
        color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] a {{
        color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {{
        color: #102A43 !important;
        border-radius: 8px !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {{
        background: #E4EEF2 !important;
    }}

    section[data-testid="stSidebar"] [aria-current="page"] {{
        background: #DCE8ED !important;
        color: #0B6670 !important;
        font-weight: 700 !important;
    }}

    section[data-testid="stSidebar"] [aria-current="page"] * {{
        color: #0B6670 !important;
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] div[data-baseweb="select"] span {{
        color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] svg {{
        fill: #486581 !important;
    }}

    div[data-baseweb="select"] > div {{
        min-height: 34px !important;
        background: #FFFFFF !important;
        color: #102A43 !important;
        border: 1px solid #C7D6DE !important;
        border-radius: 8px !important;
        box-shadow: none !important;
    }}

    div[data-baseweb="select"] > div:hover {{
        border-color: #1697A6 !important;
    }}


    div[data-testid="stDataFrame"] {{
        border: 1px solid #D3E0E7 !important;
        border-radius: 10px !important;
        background: #FFFFFF !important;
        box-shadow: 0 2px 8px rgba(16,42,67,.06) !important;
    }}

    div[data-testid="stDataFrame"] > div {{
        border-radius: 10px !important;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}


    /* ======================================================
       FINAL SIDEBAR LIGHT-THEME FIX
       These selectors target Streamlit/BaseWeb internals that can
       otherwise inherit the app's dark theme.
    ====================================================== */

    section[data-testid="stSidebar"] {{
        background: #F8FBFD !important;
        color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] > div {{
        background: #F8FBFD !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSelectbox"] {{
        color-scheme: light !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"],
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [role="combobox"],
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [aria-haspopup="listbox"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #102A43 !important;
        -webkit-text-fill-color: #102A43 !important;
        border-color: #C7D6DE !important;
        color-scheme: light !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] *,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [role="combobox"] *,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [aria-haspopup="listbox"] * {{
        color: #102A43 !important;
        -webkit-text-fill-color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stSelectbox"] svg {{
        color: #486581 !important;
        fill: #486581 !important;
    }}

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {{
        background: #FFFFFF !important;
        color: #102A43 !important;
        color-scheme: light !important;
    }}

    li[role="option"],
    li[role="option"] * {{
        background: #FFFFFF !important;
        color: #102A43 !important;
        -webkit-text-fill-color: #102A43 !important;
    }}

    li[role="option"]:hover,
    li[role="option"][aria-selected="true"] {{
        background: #E6F1F4 !important;
        color: #0B6670 !important;
        -webkit-text-fill-color: #0B6670 !important;
    }}

    /* Navigation readability */
    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"],
    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] * {{
        color: #102A43 !important;
        -webkit-text-fill-color: #102A43 !important;
    }}

    section[data-testid="stSidebar"] [aria-current="page"],
    section[data-testid="stSidebar"] [aria-current="page"] * {{
        background: #DCECEF !important;
        color: #0B6670 !important;
        -webkit-text-fill-color: #0B6670 !important;
        font-weight: 700 !important;
    }}

    /* ======================================================
       CUSTOM WATCHLIST TABLE
    ====================================================== */

    .watchlist-shell {{
        width: 100%;
        max-height: 270px;
        overflow: auto;
        background: #FFFFFF;
        border: 1px solid #D3E0E7;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(16,42,67,.06);
    }}

    table.watchlist-table {{
        width: 100%;
        min-width: 1220px;
        border-collapse: separate;
        border-spacing: 0;
        background: #FFFFFF;
        color: #102A43;
        font-size: 12px;
    }}

    .watchlist-table thead th {{
        position: sticky;
        top: 0;
        z-index: 2;
        background: #EAF2F5;
        color: #102A43;
        text-align: left;
        font-weight: 800;
        padding: 10px 10px;
        border-bottom: 1px solid #CCDCE4;
        white-space: nowrap;
    }}

    .watchlist-table tbody td {{
        background: #FFFFFF;
        color: #102A43;
        padding: 9px 10px;
        border-bottom: 1px solid #E4ECF1;
        white-space: nowrap;
        vertical-align: middle;
    }}

    .watchlist-table tbody tr:nth-child(even) td {{
        background: #F8FBFC;
    }}

    .watchlist-table tbody tr:hover td {{
        background: #EEF7F8;
    }}

    .risk-badge {{
        display: inline-flex;
        align-items: center;
        border-radius: 999px;
        padding: 4px 8px;
        font-weight: 800;
        font-size: 11px;
    }}

    .risk-high {{
        color: #B4232E;
        background: #FDECEF;
        border: 1px solid #F5C4C9;
    }}

    .risk-medium {{
        color: #0B6670;
        background: #E7F4F5;
        border: 1px solid #C4E3E6;
    }}

    .risk-low {{
        color: #0B6670;
        background: #E7F4F5;
        border: 1px solid #C4E3E6;
    }}

    .probability-cell {{
        min-width: 175px;
    }}

    .probability-row {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .probability-track {{
        flex: 1;
        min-width: 95px;
        height: 8px;
        border-radius: 999px;
        background: #E6EDF2;
        overflow: hidden;
    }}

    .probability-fill {{
        height: 100%;
        border-radius: 999px;
        background: #E6535D;
    }}

    .probability-value {{
        min-width: 44px;
        text-align: right;
        font-weight: 800;
        color: #102A43;
    }}

    </style>
    """
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_risk_data():

    possible_paths = [
        Path("telco_customer_churn_risk.csv"),
        Path("Telco_Churn_Project/telco_customer_churn_risk.csv"),
        Path("data/telco_customer_churn_risk.csv"),
    ]

    for path in possible_paths:
        if path.exists():
            return pd.read_csv(path)

    return None


df = load_risk_data()

if df is None:
    st.error("Could not find telco_customer_churn_risk.csv")
    st.stop()

df.columns = df.columns.str.strip()


# ============================================================
# COLUMN FINDER
# ============================================================

def find_column(names):

    normalized = {
        col.lower()
        .replace("_", "")
        .replace(" ", "")
        .replace("%", ""): col
        for col in df.columns
    }

    for name in names:

        key = (
            name.lower()
            .replace("_", "")
            .replace(" ", "")
            .replace("%", "")
        )

        if key in normalized:
            return normalized[key]

    return None


# ============================================================
# COLUMN DETECTION
# ============================================================

customer_col = find_column([
    "CustomerID",
    "Customer ID"
])

risk_col = find_column([
    "Risk Level",
    "RiskLevel"
])

probability_col = find_column([
    "Churn Probability",
    "Churn Probability %",
    "Probability",
    "ChurnProbability"
])

contract_col = find_column([
    "Contract"
])

internet_col = find_column([
    "Internet Service",
    "InternetService"
])

payment_col = find_column([
    "Payment Method",
    "PaymentMethod"
])

monthly_col = find_column([
    "Monthly Charges",
    "MonthlyCharges"
])

tenure_col = find_column([
    "Tenure Months",
    "Tenure"
])

cltv_col = find_column([
    "CLTV",
    "Customer Lifetime Value"
])

revenue_col = find_column([
    "Total Charges",
    "TotalCharges",
    "Revenue"
])

action_col = find_column([
    "Recommended Action",
    "RecommendedAction"
])

online_security_col = find_column([
    "Online Security",
    "OnlineSecurity"
])


# ============================================================
# NUMERIC CLEANING
# ============================================================

for col in [
    probability_col,
    monthly_col,
    tenure_col,
    cltv_col,
    revenue_col
]:
    if col:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )


# ============================================================
# PROBABILITY 0-100
# ============================================================

if probability_col:

    max_probability = df[probability_col].max()

    if (
        pd.notna(max_probability)
        and max_probability <= 1
    ):
        df["Probability_Display"] = (
            df[probability_col] * 100
        )
    else:
        df["Probability_Display"] = (
            df[probability_col]
        )

else:
    df["Probability_Display"] = np.nan


# ============================================================
# CREATE RISK LEVEL IF REQUIRED
# ============================================================

if risk_col is None:

    df["Generated Risk Level"] = pd.cut(
        df["Probability_Display"],
        bins=[
            -np.inf,
            40,
            62,
            np.inf
        ],
        labels=[
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ]
    )

    risk_col = "Generated Risk Level"


# ============================================================
# ACTION
# ============================================================

if action_col is None:

    df["Generated Action"] = np.select(
        [
            df[risk_col]
            .astype(str)
            .str.contains(
                "High",
                case=False,
                na=False
            ),

            df[risk_col]
            .astype(str)
            .str.contains(
                "Medium",
                case=False,
                na=False
            )
        ],
        [
            "Immediate retention outreach",
            "Targeted retention offer"
        ],
        default="Standard engagement"
    )

    action_col = "Generated Action"


# ============================================================
# HEADER
# ============================================================

html(
    """
    <div class="hero">

        <div class="hero-icon">
            🚨
        </div>

        <div>

            <div class="hero-title">

                High Risk Customer

                <span style="color:#1697A6;">
                    Retention Center
                </span>

            </div>

            <div class="hero-subtitle">

                CUSTOMER RISK PRIORITIZATION
                • REVENUE PROTECTION
                • RETENTION ACTIONS
                • CUSTOMER-LEVEL DECISION SUPPORT

            </div>

        </div>

    </div>
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "## 🎯 Risk Filters"
)

filtered_df = df.copy()


def sidebar_filter(
    data,
    column,
    label
):

    if column is None:
        return data

    values = (
        data[column]
        .dropna()
        .astype(str)
        .sort_values()
        .unique()
        .tolist()
    )

    selected = st.sidebar.selectbox(
        label,
        ["All"] + values
    )

    if selected != "All":
        data = data[
            data[column]
            .astype(str)
            .eq(selected)
        ]

    return data


filtered_df = sidebar_filter(
    filtered_df,
    risk_col,
    "🚦 Risk Level"
)

filtered_df = sidebar_filter(
    filtered_df,
    contract_col,
    "📄 Contract"
)

filtered_df = sidebar_filter(
    filtered_df,
    internet_col,
    "📡 Internet Service"
)

filtered_df = sidebar_filter(
    filtered_df,
    payment_col,
    "💳 Payment Method"
)


# ============================================================
# HIGH RISK DATA
# ============================================================

high_risk_mask = (
    filtered_df[risk_col]
    .astype(str)
    .str.contains(
        "High",
        case=False,
        na=False
    )
)

high_risk_df = (
    filtered_df[
        high_risk_mask
    ]
    .copy()
)


# ============================================================
# KPI CALCULATIONS
# ============================================================

high_risk_count = len(
    high_risk_df
)

avg_probability = (
    high_risk_df[
        "Probability_Display"
    ]
    .mean()
)

if revenue_col:

    revenue_at_risk = (
        high_risk_df[
            revenue_col
        ]
        .fillna(0)
        .sum()
    )

elif monthly_col:

    revenue_at_risk = (
        high_risk_df[
            monthly_col
        ]
        .fillna(0)
        .sum()
    )

else:
    revenue_at_risk = 0


avg_cltv_at_risk = (
    high_risk_df[
        cltv_col
    ]
    .mean()
    if cltv_col
    else 0
)


# ============================================================
# KPI COMPONENT
# ============================================================

def kpi(
    icon,
    value,
    label
):

    html(
        f"""
        <div class="kpi">

            <div class="kpi-top">

                <div class="kpi-icon">
                    {icon}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

            </div>

            <div class="kpi-label">
                {label}
            </div>

        </div>
        """
    )


# ============================================================
# KPI ROW
# ============================================================

html(
    '<div class="section-title">'
    '🚨 High Risk Portfolio'
    '</div>'
)

k1, k2, k3, k4 = st.columns(
    4,
    gap="medium"
)


with k1:
    kpi(
        "👥",
        f"{high_risk_count:,}",
        "High Risk Customers"
    )


with k2:

    probability_text = (
        f"{avg_probability:.1f}%"
        if pd.notna(avg_probability)
        else "N/A"
    )

    kpi(
        "🎯",
        probability_text,
        "Avg Churn Probability"
    )


with k3:

    if revenue_at_risk >= 1_000_000:
        revenue_text = (
            f"{revenue_at_risk / 1_000_000:.2f}M"
        )

    elif revenue_at_risk >= 1000:
        revenue_text = (
            f"{revenue_at_risk / 1000:.1f}K"
        )

    else:
        revenue_text = (
            f"{revenue_at_risk:.0f}"
        )

    kpi(
        "💸",
        revenue_text,
        "Revenue at Risk"
    )


with k4:

    if (
        pd.notna(avg_cltv_at_risk)
        and avg_cltv_at_risk > 0
    ):
        cltv_text = (
            f"{avg_cltv_at_risk / 1000:.2f}K"
        )
    else:
        cltv_text = "N/A"

    kpi(
        "💎",
        cltv_text,
        "Avg CLTV at Risk"
    )


# ============================================================
# CHART STYLE
# ============================================================

def chart_style(
    fig,
    title,
    height=CHART_HEIGHT,
    left=50,
    right=35,
    top=39,
    bottom=23
):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.5,
            xanchor="center",
            y=0.97,
            font=dict(
                size=CHART_TITLE_SIZE,
                color=TEXT
            )
        ),

        height=height,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=left,
            r=right,
            t=top,
            b=bottom
        ),

        font=dict(
            family="Arial",
            size=11,
            color=TEXT
        ),

        showlegend=False,

        # Prevent Plotly from shrinking trace text inconsistently.
        uniformtext=dict(
            minsize=DATA_LABEL_SIZE,
            mode="show"
        ),

        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_color=TEXT,
            font_size=11
        )
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,

        tickfont=dict(
            color=TEXT,
            size=CATEGORY_LABEL_SIZE
        ),

        title_font=dict(
            color="#486581",
            size=AXIS_TITLE_SIZE
        )
    )

    fig.update_yaxes(
        showgrid=False,
        zeroline=False,

        tickfont=dict(
            color=TEXT,
            size=CATEGORY_LABEL_SIZE
        ),

        title_font=dict(
            color="#486581",
            size=AXIS_TITLE_SIZE
        )
    )

    return fig


# ============================================================
# RISK PRIORITIZATION
# ============================================================

html(
    '<div class="row-gap"></div>'
)

html(
    '<div class="section-title">'
    '📊 Risk Prioritization'
    '</div>'
)


# ============================================================
# CHART ROW 1
# ============================================================

top_left, top_right = st.columns(
    [1.3, 1],
    gap="medium"
)


# ============================================================
# TOP HIGH-RISK CUSTOMERS
# ============================================================

with top_left:

    if (
        customer_col
        and not high_risk_df.empty
    ):

        # Keep only top 5 customers so the compact chart remains readable.
        top_risk = (
            high_risk_df
            .sort_values(
                "Probability_Display",
                ascending=False
            )
            .head(5)
            .sort_values(
                "Probability_Display",
                ascending=True
            )
        )

        fig = go.Figure()

        fig.add_bar(
            x=top_risk[
                "Probability_Display"
            ],
            y=top_risk[
                customer_col
            ],
            orientation="h",

            # Thicker, evenly spaced bars
            width=0.58,

            marker_color=TEAL,

            # Put labels inside bars so they never overlap outside
            text=[
                f"{value:.1f}%"
                for value in top_risk[
                    "Probability_Display"
                ]
            ],

            textposition="inside",

            insidetextanchor="end",

            textfont=dict(
                size=11.5,
                color=TEXT,
                family="Arial"
            ),

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>Churn Probability: %{x:.1f}%"
                "<extra></extra>"
            )
        )

        fig = chart_style(
            fig,
            "🎯 Highest Churn Probability Customers",

            left=105,
            right=22,
            top=40,
            bottom=28
        )

        # Fixed 0–100 scale keeps all percentage labels aligned.
        fig.update_xaxes(
            range=[
                0,
                100
            ],
            title=dict(
                text="Churn Probability (%)",
                font=dict(
                    size=12,
                    color="#486581"
                ),
                standoff=8
            ),
            tickvals=[0, 20, 40, 60, 80, 100],
            tickfont=dict(
                size=11.2,
                color=TEXT
            )
        )

        fig.update_yaxes(
            tickfont=dict(
                size=10.8,
                color=TEXT
            ),
            automargin=True
        )

        # Prevent Plotly from auto-shrinking the inside labels.
        fig.update_layout(
            uniformtext=dict(
                minsize=11.5,
                mode="show"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "displayModeBar": False
            }
        )


# ============================================================
# REVENUE AT RISK BY CONTRACT
# ============================================================

with top_right:

    value_col = (
        revenue_col
        if revenue_col
        else monthly_col
    )

    if (
        contract_col
        and value_col
    ):

        CONTRACT_ORDER = [
            "Month-to-month",
            "One year",
            "Two year"
        ]

        contract_risk = (
            high_risk_df
            .groupby(
                contract_col
            )[value_col]
            .sum()
            .reindex(
                CONTRACT_ORDER,
                fill_value=0
            )
            .reset_index()
        )

        fig = go.Figure()

        fig.add_bar(
            x=contract_risk[
                contract_col
            ],
            y=contract_risk[
                value_col
            ],
            width=0.38,
            marker_color=TEAL,
            hovertemplate=(
                "<b>%{x}</b>"
                "<br>Revenue at Risk: %{y:,.0f}"
                "<extra></extra>"
            )
        )

        max_contract_value = (
            contract_risk[
                value_col
            ].max()
        )

        if max_contract_value <= 0:
            max_contract_value = 1

        # Fixed readable annotations above bars, including zero.
        for _, row in contract_risk.iterrows():

            value = row[value_col]

            label = (
                f"{value / 1000:.1f}K"
                if value >= 1000
                else f"{value:.0f}"
            )

            y_pos = (
                value + max_contract_value * 0.045
                if value > 0
                else max_contract_value * 0.04
            )

            fig.add_annotation(
                x=row[contract_col],
                y=y_pos,
                text=f"<b>{label}</b>",
                showarrow=False,
                xanchor="center",
                yanchor="bottom",
                font=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT,
                    family="Arial"
                )
            )

        fig = chart_style(
            fig,
            "💸 Revenue at Risk by Contract",
            left=25,
            right=25,
            top=40,
            bottom=26
        )

        fig.update_yaxes(
            showticklabels=False,
            range=[
                0,
                max_contract_value * 1.22
            ]
        )

        fig.update_xaxes(
            categoryorder="array",
            categoryarray=CONTRACT_ORDER,

            tickfont=dict(
                size=10.3,
                color=TEXT
            )
        )

        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "displayModeBar": False
            }
        )


# ============================================================
# CHART ROW 2
# ============================================================

html(
    '<div class="row-gap"></div>'
)

bottom_left, bottom_right = st.columns(
    [1.1, 1],
    gap="medium"
)


# ============================================================
# RETENTION ACTIONS
# ============================================================

with bottom_left:

    action_summary = (
        filtered_df[
            action_col
        ]
        .fillna(
            "No Action Assigned"
        )
        .value_counts()
        .head(6)
        .sort_values()
    )

    fig = go.Figure()

    fig.add_bar(
        x=action_summary.values,
        y=action_summary.index,
        orientation="h",
        width=0.45,
        marker_color=TEAL,
        hovertemplate=(
            "<b>%{y}</b>"
            "<br>Customers: %{x}"
            "<extra></extra>"
        )
    )

    max_action = (
        action_summary.max()
        if len(action_summary)
        else 1
    )

    # Fixed annotations instead of trace text.
    for action_name, value in action_summary.items():

        fig.add_annotation(
            x=value + max_action * 0.012,
            y=action_name,
            text=f"<b>{int(value):,}</b>",
            showarrow=False,
            xanchor="left",
            yanchor="middle",
            font=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT,
                family="Arial"
            )
        )

    fig = chart_style(
        fig,
        "🛠 Recommended Retention Actions",
        left=190,
        right=55,
        top=40,
        bottom=12
    )

    fig.update_xaxes(
        showticklabels=False,
        range=[
            0,
            max_action * 1.13
        ]
    )

    fig.update_yaxes(
        tickfont=dict(
            size=10.2,
            color=TEXT
        )
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )


# ============================================================
# RISK DISTRIBUTION
# ============================================================

with bottom_right:

    risk_summary = (
        filtered_df[
            risk_col
        ]
        .astype(str)
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "Risk",
        "Customers"
    ]

    RISK_ORDER = [
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]

    risk_summary = (
        risk_summary
        .set_index(
            "Risk"
        )
        .reindex(
            RISK_ORDER,
            fill_value=0
        )
        .reset_index()
    )

    # Consistent dashboard palette:
    # teal for normal portfolio categories; red only for genuine high-risk emphasis.
    color_map = {
        "Low Risk": TEAL,
        "Medium Risk": TEAL,
        "High Risk": RED
    }

    colors = [
        color_map.get(
            risk,
            TEAL
        )
        for risk in
        risk_summary[
            "Risk"
        ]
    ]

    fig = go.Figure()

    fig.add_bar(
        x=risk_summary[
            "Risk"
        ],
        y=risk_summary[
            "Customers"
        ],
        width=0.42,
        marker_color=colors,
        hovertemplate=(
            "<b>%{x}</b>"
            "<br>Customers: %{y}"
            "<extra></extra>"
        )
    )

    max_customers = (
        risk_summary[
            "Customers"
        ].max()
    )

    if max_customers <= 0:
        max_customers = 1

    # Fixed large values above each column.
    for _, row in risk_summary.iterrows():

        fig.add_annotation(
            x=row["Risk"],
            y=row["Customers"] + max_customers * 0.035,
            text=f"<b>{int(row['Customers']):,}</b>",
            showarrow=False,
            xanchor="center",
            yanchor="bottom",
            font=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT,
                family="Arial"
            )
        )

    fig = chart_style(
        fig,
        "🚦 Customer Risk Distribution",
        left=25,
        right=25,
        top=40,
        bottom=22
    )

    fig.update_yaxes(
        showticklabels=False,
        range=[
            0,
            max_customers * 1.18
        ]
    )

    fig.update_xaxes(
        categoryorder="array",
        categoryarray=RISK_ORDER,

        tickfont=dict(
            size=10.5,
            color=TEXT
        )
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )


# ============================================================
# WATCHLIST TITLE
# ============================================================

html(
    '<div class="row-gap"></div>'
)

html(
    """
    <div class="watch-title">
        📋 High Risk Customer Watchlist
    </div>
    """
)


# ============================================================
# WATCHLIST COLUMNS
# ============================================================

watch_columns = []

for col in [
    customer_col,
    risk_col,
    probability_col,
    contract_col,
    internet_col,
    payment_col,
    monthly_col,
    tenure_col,
    cltv_col,
    online_security_col,
    action_col
]:

    if (
        col is not None
        and col not in watch_columns
    ):
        watch_columns.append(
            col
        )


watch_df = (
    high_risk_df[
        watch_columns
    ]
    .copy()
)


# ============================================================
# RENAME WATCHLIST
# ============================================================

rename_map = {}

if customer_col:
    rename_map[
        customer_col
    ] = "Customer ID"

if risk_col:
    rename_map[
        risk_col
    ] = "Risk Level"

if probability_col:
    rename_map[
        probability_col
    ] = "Churn Probability"

if contract_col:
    rename_map[
        contract_col
    ] = "Contract"

if internet_col:
    rename_map[
        internet_col
    ] = "Internet Service"

if payment_col:
    rename_map[
        payment_col
    ] = "Payment Method"

if monthly_col:
    rename_map[
        monthly_col
    ] = "Monthly Charges"

if tenure_col:
    rename_map[
        tenure_col
    ] = "Tenure"

if cltv_col:
    rename_map[
        cltv_col
    ] = "CLTV"

if online_security_col:
    rename_map[
        online_security_col
    ] = "Online Security"

if action_col:
    rename_map[
        action_col
    ] = "Recommended Action"


watch_df = (
    watch_df
    .rename(
        columns=rename_map
    )
)


# ============================================================
# CLEAN WATCHLIST
# ============================================================

if probability_col:

    watch_df[
        "Churn Probability"
    ] = (
        high_risk_df[
            "Probability_Display"
        ]
        .round(1)
    )


if (
    "Monthly Charges"
    in watch_df.columns
):

    watch_df[
        "Monthly Charges"
    ] = (
        watch_df[
            "Monthly Charges"
        ]
        .round(2)
    )


if (
    "CLTV"
    in watch_df.columns
):

    watch_df[
        "CLTV"
    ] = (
        watch_df[
            "CLTV"
        ]
        .round(0)
        .astype(
            "Int64"
        )
    )


if (
    "Tenure"
    in watch_df.columns
):

    watch_df[
        "Tenure"
    ] = (
        watch_df[
            "Tenure"
        ]
        .round(0)
        .astype(
            "Int64"
        )
    )


# ============================================================
# SORT WATCHLIST
# ============================================================

if (
    "Churn Probability"
    in watch_df.columns
):

    watch_df = (
        watch_df
        .sort_values(
            "Churn Probability",
            ascending=False
        )
    )


# ============================================================
# COLUMN CONFIG
# ============================================================

column_config = {}


if (
    "Customer ID"
    in watch_df.columns
):

    column_config[
        "Customer ID"
    ] = st.column_config.TextColumn(
        "Customer ID",
        width="small"
    )


if (
    "Risk Level"
    in watch_df.columns
):

    column_config[
        "Risk Level"
    ] = st.column_config.TextColumn(
        "Risk Level",
        width="small"
    )


if (
    "Churn Probability"
    in watch_df.columns
):

    column_config[
        "Churn Probability"
    ] = st.column_config.ProgressColumn(
        "Churn Probability",
        min_value=0,
        max_value=100,
        format="%.1f%%",
        width="medium"
    )


if (
    "Contract"
    in watch_df.columns
):

    column_config[
        "Contract"
    ] = st.column_config.TextColumn(
        "Contract",
        width="small"
    )


if (
    "Internet Service"
    in watch_df.columns
):

    column_config[
        "Internet Service"
    ] = st.column_config.TextColumn(
        "Internet Service",
        width="small"
    )


if (
    "Payment Method"
    in watch_df.columns
):

    column_config[
        "Payment Method"
    ] = st.column_config.TextColumn(
        "Payment Method",
        width="medium"
    )


if (
    "Monthly Charges"
    in watch_df.columns
):

    column_config[
        "Monthly Charges"
    ] = st.column_config.NumberColumn(
        "Monthly Charges",
        format="$%.2f",
        width="small"
    )


if (
    "Tenure"
    in watch_df.columns
):

    column_config[
        "Tenure"
    ] = st.column_config.NumberColumn(
        "Tenure",
        width="small"
    )


if (
    "CLTV"
    in watch_df.columns
):

    column_config[
        "CLTV"
    ] = st.column_config.NumberColumn(
        "CLTV",
        format="%d",
        width="small"
    )


if (
    "Online Security"
    in watch_df.columns
):

    column_config[
        "Online Security"
    ] = st.column_config.TextColumn(
        "Online Security",
        width="small"
    )


if (
    "Recommended Action"
    in watch_df.columns
):

    column_config[
        "Recommended Action"
    ] = st.column_config.TextColumn(
        "Recommended Action",
        width="large"
    )


# ============================================================
# DISPLAY WATCHLIST
# ============================================================

def render_watchlist_table(dataframe):

    if dataframe.empty:
        html(
            """
            <div style="
                background:#FFFFFF;
                border:1px solid #D3E0E7;
                border-radius:10px;
                padding:18px;
                color:#486581;
                text-align:center;
            ">
                No high-risk customers match the selected filters.
            </div>
            """
        )
        return

    display_df = dataframe.copy()

    headers = "".join(
        f"<th>{html_lib.escape(str(col))}</th>"
        for col in display_df.columns
    )

    rows = []

    for _, row in display_df.iterrows():

        cells = []

        for col in display_df.columns:

            value = row[col]

            if pd.isna(value):
                value = ""

            if col == "Risk Level":

                risk_text = str(value)
                risk_class = (
                    "risk-high"
                    if risk_text.lower().startswith("high")
                    else "risk-medium"
                    if risk_text.lower().startswith("medium")
                    else "risk-low"
                )

                cell_html = (
                    f'<span class="risk-badge {risk_class}">'
                    f'{html_lib.escape(risk_text)}'
                    f'</span>'
                )

            elif col == "Churn Probability":

                try:
                    probability = float(value)
                except Exception:
                    probability = 0.0

                probability = max(
                    0.0,
                    min(
                        100.0,
                        probability
                    )
                )

                cell_html = f"""
                    <div class="probability-cell">
                        <div class="probability-row">
                            <div class="probability-track">
                                <div
                                    class="probability-fill"
                                    style="width:{probability:.1f}%;">
                                </div>
                            </div>
                            <div class="probability-value">
                                {probability:.1f}%
                            </div>
                        </div>
                    </div>
                """

            elif col == "Monthly Charges":

                try:
                    cell_html = f"${float(value):,.2f}"
                except Exception:
                    cell_html = html_lib.escape(str(value))

            elif col == "CLTV":

                try:
                    cell_html = f"{int(float(value)):,}"
                except Exception:
                    cell_html = html_lib.escape(str(value))

            elif col == "Tenure":

                try:
                    cell_html = f"{int(float(value))}"
                except Exception:
                    cell_html = html_lib.escape(str(value))

            else:

                cell_html = html_lib.escape(
                    str(value)
                )

            cells.append(
                f"<td>{cell_html}</td>"
            )

        rows.append(
            "<tr>"
            + "".join(cells)
            + "</tr>"
        )

    table_html = f"""
        <div class="watchlist-shell">
            <table class="watchlist-table">
                <thead>
                    <tr>
                        {headers}
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows)}
                </tbody>
            </table>
        </div>
    """

    html(table_html)


render_watchlist_table(
    watch_df
)
