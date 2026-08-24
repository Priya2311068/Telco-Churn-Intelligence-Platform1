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
    page_title="Customer Segment & Revenue Analysis",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL COLOR SYSTEM
# ============================================================

# Slightly darker page background
BG = "#E9EFF5"

# Cards
CARD = "#FFFFFF"
CARD_2 = "#F1F5F9"
BORDER = "#D7E2EC"

# Main dashboard accent
TEAL = "#145B8F"

# Red ONLY for churn / negative / high-risk state
RED = "#E0525E"

# Typography
TEXT = "#16324F"
MUTED = "#64748B"


# ============================================================
# VISUAL SETTINGS
# ============================================================

# Increased for readability
DATA_LABEL_SIZE = 13
CATEGORY_LABEL_SIZE = 11.5
AXIS_TITLE_SIZE = 11
CHART_TITLE_SIZE = 14

KPI_HEIGHT = 78
MINI_HEIGHT = 145
MAIN_HEIGHT = 175
MATRIX_HEIGHT = 190
BOTTOM_HEIGHT = 112

MINI_BAR_WIDTH = 0.28
ROW_GAP = 7


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

    /* ======================================================
       MAIN APP
    ====================================================== */

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    html,
    body,
    [data-testid="stAppViewContainer"] {{
        background: {BG} !important;
        color: {TEXT} !important;
    }}


    /* ======================================================
       PAGE LAYOUT
    ====================================================== */

    .block-container {{
        max-width: 1650px !important;
        padding-top: 0.10rem !important;
        padding-bottom: 0.10rem !important;
        padding-left: 0.50rem !important;
        padding-right: 0.50rem !important;
    }}


    /* ======================================================
       STREAMLIT HEADER
    ====================================================== */

    header[data-testid="stHeader"] {{
        height: 22px !important;
        min-height: 22px !important;
        background: transparent !important;
    }}


    /* ======================================================
       HERO
    ====================================================== */

    .hero {{
        height: 58px;
        box-sizing: border-box;

        padding: 7px 13px;

        display: flex;
        align-items: center;

        border: 1px solid {BORDER};
        border-radius: 12px;

        background:
            linear-gradient(
                120deg,
                #FFFFFF,
                #F5F9FD
            );

        box-shadow:
            0px 4px 12px
            rgba(15,47,79,.07);

        margin-bottom: 3px;
    }}


    .hero-icon {{
        height: 36px;
        width: 36px;
        min-width: 36px;

        margin-right: 10px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 9px;

        font-size: 18px;

        background:
            rgba(20,91,143,.12);
    }}


    .hero-title {{
        font-size: 22px;
        font-weight: 850;
        line-height: 1;

        color: {TEXT};
    }}


    .hero-subtitle {{
        margin-top: 4px;

        font-size: 8px;
        letter-spacing: .75px;

        color: {MUTED};
    }}


    /* ======================================================
       SECTION TITLES
    ====================================================== */

    .section-title {{
        color: {TEAL};

        font-size: 12.8px;
        font-weight: 850;
        line-height: 1;

        margin-top: 4px;
        margin-bottom: 4px;
    }}


    .row-gap {{
        height: {ROW_GAP}px;
    }}


    /* ======================================================
       KPI CARDS
    ====================================================== */

    .kpi {{
        height: {KPI_HEIGHT}px;

        box-sizing: border-box;

        padding: 8px 11px;

        border: 1px solid {BORDER};
        border-radius: 11px;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

        box-shadow:
            0px 4px 12px
            rgba(15,47,79,.07);
    }}


    .kpi-top {{
        display: flex;
        align-items: center;
        gap: 9px;
    }}


    .kpi-icon {{
        width: 26px;
        height: 26px;
        min-width: 26px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 7px;

        font-size: 14px;

        background:
            rgba(20,91,143,.11);
    }}


    .kpi-value {{
        font-size: 20px;
        font-weight: 850;
        line-height: 1;

        color: {TEXT};
    }}


    .kpi-label {{
        margin-top: 7px;

        font-size: 10px;

        color: {MUTED};
    }}


    /* ======================================================
       BOTTOM CARDS
    ====================================================== */

    .bottom-card {{
        height: {BOTTOM_HEIGHT}px;

        box-sizing: border-box;

        padding: 10px 13px;

        border: 1px solid {BORDER};
        border-radius: 11px;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

        box-shadow:
            0px 4px 12px
            rgba(15,47,79,.07);

        overflow: hidden;
    }}


    .bottom-heading {{
        margin-bottom: 6px;

        font-size: 13px;
        font-weight: 850;

        color: {TEAL};
    }}


    .bottom-text {{
        font-size: 12px;
        line-height: 1.30;

        color: {TEXT};
    }}


    .insight-line {{
        margin-bottom: 4px;
    }}


    .highlight {{
        color: {TEAL};
        font-weight: 850;
    }}


    /* ======================================================
       PLOTLY CHART CARDS
    ====================================================== */

    div[data-testid="stPlotlyChart"] {{
        border: 1px solid {BORDER};
        border-radius: 11px;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

        overflow: hidden;

        box-shadow:
            0px 4px 12px
            rgba(15,47,79,.08);
    }}


    /* ======================================================
       SPACING
    ====================================================== */

    div[data-testid="stVerticalBlock"] {{
        gap: 0.08rem !important;
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
        background: #FFFFFF !important;

        border-right:
            1px solid {BORDER};
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

        -webkit-text-fill-color:
            {TEXT} !important;
    }}


    /* ======================================================
       FILTER SELECTBOXES
    ====================================================== */

    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div {{

        min-height: 38px !important;

        background:
            #FFFFFF !important;

        color:
            {TEXT} !important;

        border:
            1px solid #C9D6E2 !important;

        border-radius:
            8px !important;

        box-shadow:
            0 2px 6px
            rgba(15,47,79,.04) !important;
    }}


    section[data-testid="stSidebar"]
    [role="combobox"] {{

        background:
            #FFFFFF !important;

        color:
            {TEXT} !important;

        -webkit-text-fill-color:
            {TEXT} !important;
    }}


    section[data-testid="stSidebar"]
    div[data-baseweb="select"] span {{

        color:
            {TEXT} !important;

        -webkit-text-fill-color:
            {TEXT} !important;
    }}


    section[data-testid="stSidebar"]
    div[data-baseweb="select"] svg {{

        fill:
            {MUTED} !important;

        color:
            {MUTED} !important;
    }}


    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div:hover {{

        border-color:
            {TEAL} !important;
    }}


    section[data-testid="stSidebar"]
    div[data-baseweb="select"] > div:focus-within {{

        border-color:
            {TEAL} !important;

        box-shadow:
            0 0 0 1px
            {TEAL} !important;
    }}


    /* ======================================================
       DROPDOWN
    ====================================================== */

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {{

        color-scheme: light !important;

        background:
            #FFFFFF !important;

        color:
            {TEXT} !important;
    }}


    li[role="option"],
    li[role="option"] * {{

        background:
            #FFFFFF !important;

        color:
            {TEXT} !important;

        -webkit-text-fill-color:
            {TEXT} !important;
    }}


    li[role="option"]:hover {{

        background:
            #EAF5FD !important;

        color:
            {TEAL} !important;
    }}


    li[role="option"][aria-selected="true"] {{

        background:
            #DCEFFD !important;

        color:
            {TEAL} !important;
    }}


    /* ======================================================
       HIDE STREAMLIT ELEMENTS
    ====================================================== */

    #MainMenu {{
        visibility: hidden;
    }}


    footer {{
        visibility: hidden;
    }}

    </style>
    """
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    paths = [

        Path(
            "telco_customer_churn.csv"
        ),

        Path(
            "Telco_Churn_Project/"
            "telco_customer_churn.csv"
        ),

        Path(
            "data/"
            "telco_customer_churn.csv"
        ),
    ]


    for path in paths:

        if path.exists():

            return pd.read_csv(
                path
            )


    return None


df = load_data()


if df is None:

    st.error(
        "Could not find "
        "telco_customer_churn.csv"
    )

    st.stop()


df.columns = (
    df.columns
    .str.strip()
)


# ============================================================
# COLUMN FINDER
# ============================================================

def find_column(names):

    normalized = {

        col.lower()
        .replace("_", "")
        .replace(" ", ""):
        col

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


churn_col = find_column(
    [
        "Churn",
        "Churn Label",
        "Churn Value",
        "Customer Status"
    ]
)


monthly_col = find_column(
    [
        "MonthlyCharges",
        "Monthly Charges"
    ]
)


total_col = find_column(
    [
        "TotalCharges",
        "Total Charges"
    ]
)


cltv_col = find_column(
    [
        "CLTV",
        "Customer Lifetime Value"
    ]
)


payment_col = find_column(
    [
        "PaymentMethod",
        "Payment Method"
    ]
)


contract_col = find_column(
    [
        "Contract"
    ]
)


internet_col = find_column(
    [
        "InternetService",
        "Internet Service"
    ]
)


gender_col = find_column(
    [
        "Gender"
    ]
)


tenure_col = find_column(
    [
        "Tenure",
        "Tenure Months"
    ]
)


dependents_col = find_column(
    [
        "Dependents"
    ]
)


senior_col = find_column(
    [
        "Senior Citizen",
        "SeniorCitizen",
        "Senior Citizen Status"
    ]
)


# ============================================================
# NUMERIC CLEANING
# ============================================================

for col in [

    monthly_col,
    total_col,
    cltv_col,
    tenure_col

]:

    if col:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )


# ============================================================
# CHURN FLAG
# ============================================================

def create_churn_flag(data):

    if churn_col is None:

        return pd.Series(
            0,
            index=data.index
        )


    values = (

        data[churn_col]

        .astype(str)

        .str.lower()

        .str.strip()
    )


    return values.isin(
        [
            "yes",
            "churned",
            "1",
            "true"
        ]
    ).astype(int)


df["Churn_Flag"] = (
    create_churn_flag(df)
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "## 🔎 Filters"
)


st.sidebar.caption(
    "Explore customer segments and revenue interactively."
)


filtered_df = df.copy()


def add_filter(
    data,
    column,
    label
):

    if column is None:

        return data


    options = (

        data[column]

        .dropna()

        .astype(str)

        .sort_values()

        .unique()

        .tolist()
    )


    selected = (
        st.sidebar.selectbox(
            label,
            ["All"] + options
        )
    )


    if selected != "All":

        data = data[

            data[column]

            .astype(str)

            .eq(selected)
        ]


    return data


filtered_df = add_filter(
    filtered_df,
    internet_col,
    "📡 Internet Service"
)


filtered_df = add_filter(
    filtered_df,
    payment_col,
    "💳 Payment Method"
)


filtered_df = add_filter(
    filtered_df,
    contract_col,
    "📄 Contract"
)


filtered_df = add_filter(
    filtered_df,
    gender_col,
    "👤 Gender"
)


# ============================================================
# HEADER
# ============================================================

html(
    f"""
    <div class="hero">

        <div class="hero-icon">
            💰
        </div>

        <div>

            <div class="hero-title">

                Telco Customer

                <span style="color:{TEAL};">
                    Segment & Revenue Analysis
                </span>

            </div>

            <div class="hero-subtitle">

                CUSTOMER CHARACTERISTICS
                • REVENUE BEHAVIOR
                • VALUE SEGMENTATION
                • RETENTION OPPORTUNITIES

            </div>

        </div>

    </div>
    """
)


# ============================================================
# KPI VALUES
# ============================================================

total_revenue = (

    filtered_df[
        total_col
    ]

    .fillna(0)

    .sum()

    if total_col

    else 0
)


avg_total_charges = (

    filtered_df[
        total_col
    ]

    .mean()

    if total_col

    else 0
)


avg_monthly_charges = (

    filtered_df[
        monthly_col
    ]

    .mean()

    if monthly_col

    else 0
)


avg_cltv = (

    filtered_df[
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
# STANDARD CHART STYLE
# ============================================================

def style_chart(
    fig,
    title,
    height,
    show_x=True,
    show_y=True,
    left=40,
    right=28,
    top=43,
    bottom=25
):

    fig.update_layout(

        title=dict(

            text=title,

            x=0.5,

            xanchor="center",

            font=dict(
                size=CHART_TITLE_SIZE,
                color=TEAL
            )
        ),

        height=height,

        paper_bgcolor=
            "rgba(0,0,0,0)",

        plot_bgcolor=
            "rgba(0,0,0,0)",

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

        bargap=0.12,

        hoverlabel=dict(
            bgcolor=CARD_2,
            font_color=TEXT,
            font_size=12
        ),

        uniformtext=dict(
            minsize=DATA_LABEL_SIZE,
            mode="show"
        )
    )


    fig.update_xaxes(

        showgrid=False,

        zeroline=False,

        showticklabels=
            show_x,

        tickfont=dict(
            size=CATEGORY_LABEL_SIZE,
            color=TEXT
        )
    )


    fig.update_yaxes(

        showgrid=False,

        zeroline=False,

        showticklabels=
            show_y,

        tickfont=dict(
            size=CATEGORY_LABEL_SIZE,
            color=TEXT
        )
    )


    return fig


# ============================================================
# KPI ROW
# ============================================================

html(
    '<div class="section-title">'
    '💰 Revenue & Customer Value'
    '</div>'
)


k1, k2, k3, k4 = (
    st.columns(
        4,
        gap="medium"
    )
)


with k1:

    kpi(
        "💰",
        f"{total_revenue / 1_000_000:.2f}M",
        "Total Revenue"
    )


with k2:

    kpi(
        "💳",
        f"{avg_total_charges / 1000:.2f}K",
        "Average Total Charges"
    )


with k3:

    kpi(
        "🧾",
        f"${avg_monthly_charges:.2f}",
        "Average Monthly Charges"
    )


with k4:

    kpi(
        "💎",
        f"{avg_cltv / 1000:.2f}K",
        "Average CLTV"
    )


# ============================================================
# ROW 2
# ============================================================

html(
    '<div class="row-gap"></div>'
)


revenue_box, dependent_box, senior_box = (
    st.columns(
        3,
        gap="medium"
    )
)


# ============================================================
# AVG REVENUE BY CHURN
# ============================================================

with revenue_box:

    if total_col:

        revenue_status = (

            filtered_df

            .groupby(
                "Churn_Flag"
            )[total_col]

            .mean()

            .reset_index()
        )


        revenue_status[
            "Status"
        ] = (

            revenue_status[
                "Churn_Flag"
            ]

            .map(
                {
                    0: "No",
                    1: "Yes"
                }
            )
        )


        fig = go.Figure()


        # Red ONLY for churned Yes.
        # Teal for retained No.
        bar_colors = [

            RED if status == "Yes"
            else TEAL

            for status in
            revenue_status["Status"]
        ]


        fig.add_bar(

            x=revenue_status[
                "Status"
            ],

            y=revenue_status[
                total_col
            ],

            width=MINI_BAR_WIDTH,

            marker_color=bar_colors,

            text=[
                f"{x / 1000:.1f}K"

                for x in

                revenue_status[
                    total_col
                ]
            ],

            textposition=
                "outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>Churn: %{x}</b>"
                "<br>"
                "Average Revenue: %{y:,.2f}"
                "<extra></extra>"
            )
        )


        fig = style_chart(

            fig,

            "💵 Average Revenue by Churn Status",

            MINI_HEIGHT,

            show_y=False,

            left=30,
            right=30,
            top=48,
            bottom=15
        )


        fig.update_yaxes(

            range=[
                0,

                revenue_status[
                    total_col
                ].max()
                * 1.34
            ]
        )


        st.plotly_chart(

            fig,

            width="stretch",

            config={
                "displayModeBar":
                    False
            }
        )


# ============================================================
# DEPENDENTS
# ============================================================

with dependent_box:

    if dependents_col:

        dep_data = (

            filtered_df

            .groupby(
                dependents_col
            )[
                "Churn_Flag"
            ]

            .mean()

            .mul(100)

            .reset_index()
        )


        fig = go.Figure()


        fig.add_bar(

            x=dep_data[
                dependents_col
            ],

            y=dep_data[
                "Churn_Flag"
            ],

            width=MINI_BAR_WIDTH,

            marker_color=TEAL,

            text=[
                f"{x:.2f}%"

                for x in

                dep_data[
                    "Churn_Flag"
                ]
            ],

            textposition=
                "outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>Dependents: %{x}</b>"
                "<br>"
                "Churn Rate: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        fig = style_chart(

            fig,

            "👨‍👩‍👧 Churn Rate by Dependents",

            MINI_HEIGHT,

            show_y=False,

            left=30,
            right=30,
            top=48,
            bottom=15
        )


        fig.update_yaxes(

            range=[
                0,

                max(
                    40,

                    dep_data[
                        "Churn_Flag"
                    ].max()
                    * 1.32
                )
            ]
        )


        st.plotly_chart(

            fig,

            width="stretch",

            config={
                "displayModeBar":
                    False
            }
        )


# ============================================================
# SENIOR CITIZEN
# ============================================================

with senior_box:

    if senior_col:

        senior_data = (

            filtered_df

            .groupby(
                senior_col
            )[
                "Churn_Flag"
            ]

            .mean()

            .mul(100)

            .reset_index()
        )


        senior_data[
            "Status"
        ] = (

            senior_data[
                senior_col
            ]

            .astype(str)

            .replace(
                {
                    "1": "Yes",
                    "0": "No",
                    "1.0": "Yes",
                    "0.0": "No"
                }
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=senior_data[
                "Status"
            ],

            y=senior_data[
                "Churn_Flag"
            ],

            width=MINI_BAR_WIDTH,

            # Changed from purple to teal
            marker_color=TEAL,

            text=[
                f"{x:.2f}%"

                for x in

                senior_data[
                    "Churn_Flag"
                ]
            ],

            textposition=
                "outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>Senior Citizen: %{x}</b>"
                "<br>"
                "Churn Rate: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        fig = style_chart(

            fig,

            "👴 Churn Rate by Senior Citizen",

            MINI_HEIGHT,

            show_y=False,

            left=30,
            right=30,
            top=48,
            bottom=15
        )


        fig.update_yaxes(

            range=[
                0,

                max(
                    55,

                    senior_data[
                        "Churn_Flag"
                    ].max()
                    * 1.30
                )
            ]
        )


        st.plotly_chart(

            fig,

            width="stretch",

            config={
                "displayModeBar":
                    False
            }
        )


# ============================================================
# ROW 3
# ============================================================

html(
    '<div class="row-gap"></div>'
)


payment_box, cltv_box = (
    st.columns(
        [
            1.55,
            1
        ],
        gap="medium"
    )
)


# ============================================================
# PAYMENT METHOD
# ============================================================

with payment_box:

    if payment_col:

        payment_data = (

            filtered_df

            .groupby(
                payment_col
            )[
                "Churn_Flag"
            ]

            .mean()

            .mul(100)

            .reset_index()

            .sort_values(
                "Churn_Flag",
                ascending=True
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=payment_data[
                "Churn_Flag"
            ],

            y=payment_data[
                payment_col
            ],

            orientation="h",

            width=0.38,

            marker_color=TEAL,

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>"
                "Churn Rate: %{x:.2f}%"
                "<extra></extra>"
            )
        )


        max_payment = (

            payment_data[
                "Churn_Flag"
            ]

            .max()
        )


        for _, row in (
            payment_data.iterrows()
        ):

            fig.add_annotation(

                x=(
                    row[
                        "Churn_Flag"
                    ]

                    + max_payment
                    * 0.018
                ),

                y=row[
                    payment_col
                ],

                text=(
                    f"<b>"
                    f"{row['Churn_Flag']:.2f}%"
                    f"</b>"
                ),

                showarrow=False,

                xanchor="left",

                font=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT
                )
            )


        fig = style_chart(

            fig,

            "💳 Churn Rate by Payment Method",

            MAIN_HEIGHT,

            show_x=False,

            left=170,
            right=55,
            top=50,
            bottom=12
        )


        fig.update_xaxes(

            range=[
                0,
                max_payment
                * 1.19
            ]
        )


        fig.update_yaxes(

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
                color=TEXT
            ),

            automargin=True
        )


        st.plotly_chart(

            fig,

            width="stretch",

            config={
                "displayModeBar":
                    False
            }
        )


# ============================================================
# CLTV
# ============================================================

with cltv_box:

    if tenure_col and cltv_col:

        temp = (
            filtered_df.copy()
        )


        temp[
            "Tenure Group"
        ] = pd.cut(

            temp[
                tenure_col
            ],

            bins=[
                -1,
                12,
                24,
                48,
                np.inf
            ],

            labels=[
                "0–12 Months",
                "13–24 Months",
                "25–48 Months",
                "49+ Months"
            ]
        )


        cltv_data = (

            temp

            .groupby(
                "Tenure Group",
                observed=False
            )[
                cltv_col
            ]

            .mean()

            .reset_index()

            .sort_values(
                cltv_col,
                ascending=True
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=cltv_data[
                cltv_col
            ],

            y=cltv_data[
                "Tenure Group"
            ],

            orientation="h",

            width=0.38,

            # Changed from purple to teal
            marker_color=TEAL,

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>"
                "Average CLTV: %{x:,.2f}"
                "<extra></extra>"
            )
        )


        max_cltv = (

            cltv_data[
                cltv_col
            ]

            .max()
        )


        for _, row in (
            cltv_data.iterrows()
        ):

            fig.add_annotation(

                x=(
                    row[
                        cltv_col
                    ]

                    + max_cltv
                    * 0.018
                ),

                y=row[
                    "Tenure Group"
                ],

                text=(
                    f"<b>"
                    f"{row[cltv_col] / 1000:.2f}K"
                    f"</b>"
                ),

                showarrow=False,

                xanchor="left",

                font=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT
                )
            )


        fig = style_chart(

            fig,

            "⏳ Average CLTV by Tenure Group",

            MAIN_HEIGHT,

            show_x=False,

            left=120,
            right=55,
            top=50,
            bottom=12
        )


        fig.update_xaxes(

            range=[
                0,
                max_cltv
                * 1.18
            ]
        )


        fig.update_yaxes(

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
                color=TEXT
            ),

            automargin=True
        )


        st.plotly_chart(

            fig,

            width="stretch",

            config={
                "displayModeBar":
                    False
            }
        )


# ============================================================
# ROW 4 — FULL WIDTH MATRIX
# ============================================================

html(
    '<div class="row-gap"></div>'
)


if contract_col and payment_col:

    matrix_data = (

        filtered_df

        .groupby(
            [
                contract_col,
                payment_col
            ]
        )[
            "Churn_Flag"
        ]

        .mean()

        .mul(100)

        .reset_index()
    )


    pivot = (
        matrix_data.pivot(
            index=contract_col,
            columns=payment_col,
            values="Churn_Flag"
        )
    )


    preferred_contract_order = [
        "Month-to-month",
        "One year",
        "Two year"
    ]


    available = [

        x

        for x in
        preferred_contract_order

        if x in
        pivot.index
    ]


    if available:

        pivot = (
            pivot.loc[
                available
            ]
        )


    matrix_text = [

        [

            (
                f"{value:.2f}%"

                if pd.notna(value)

                else ""
            )

            for value in row

        ]

        for row in
        pivot.values
    ]


    # Teal-only gradient for professional consistency
    fig = go.Figure(

        go.Heatmap(

            z=pivot.values,

            x=pivot.columns,

            y=pivot.index,

            text=matrix_text,

            texttemplate=
                "%{text}",

            textfont=dict(
                size=13,
                color=TEXT
            ),

            colorscale=[
                [
                    0,
                    "#EDF7FA"
                ],
                [
                    0.50,
                    "#7FB5C7"
                ],
                [
                    1,
                    TEAL
                ]
            ],

            showscale=False,

            xgap=2,
            ygap=2,

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>"
                "%{x}"
                "<br>"
                "Churn Rate: %{z:.2f}%"
                "<extra></extra>"
            )
        )
    )


    fig = style_chart(

        fig,

        (
            "🧩 Churn Rate by Contract "
            "& Payment Method"
        ),

        MATRIX_HEIGHT,

        left=115,
        right=35,
        top=50,
        bottom=38
    )


    fig.update_xaxes(

        side="bottom",

        tickfont=dict(
            size=CATEGORY_LABEL_SIZE,
            color=TEXT
        ),

        automargin=True
    )


    fig.update_yaxes(

        autorange="reversed",

        tickfont=dict(
            size=CATEGORY_LABEL_SIZE,
            color=TEXT
        ),

        automargin=True
    )


    st.plotly_chart(

        fig,

        width="stretch",

        config={
            "displayModeBar":
                False
        }
    )


# ============================================================
# INSIGHT CALCULATIONS
# ============================================================

highest_payment_name = "N/A"

highest_payment_rate = 0


if payment_col:

    pay_summary = (

        filtered_df

        .groupby(
            payment_col
        )[
            "Churn_Flag"
        ]

        .mean()

        .mul(100)
    )


    if not pay_summary.empty:

        highest_payment_name = (
            pay_summary.idxmax()
        )

        highest_payment_rate = (
            pay_summary.max()
        )


best_cltv_group = "N/A"

best_cltv_value = 0


if tenure_col and cltv_col:

    insight_temp = (
        filtered_df.copy()
    )


    insight_temp[
        "Tenure Group"
    ] = pd.cut(

        insight_temp[
            tenure_col
        ],

        bins=[
            -1,
            12,
            24,
            48,
            np.inf
        ],

        labels=[
            "0–12 Months",
            "13–24 Months",
            "25–48 Months",
            "49+ Months"
        ]
    )


    cltv_summary = (

        insight_temp

        .groupby(
            "Tenure Group",
            observed=False
        )[
            cltv_col
        ]

        .mean()
    )


    if not cltv_summary.empty:

        best_cltv_group = str(
            cltv_summary.idxmax()
        )

        best_cltv_value = (
            cltv_summary.max()
        )


# ============================================================
# BOTTOM ROW
# ============================================================

html(
    '<div class="row-gap"></div>'
)


insight_box, recommendation_box = (
    st.columns(
        2,
        gap="medium"
    )
)


# ============================================================
# KEY INSIGHTS
# ============================================================

with insight_box:

    html(
        f"""
        <div class="bottom-card">

            <div class="bottom-heading">

                💡 KEY INSIGHTS

            </div>

            <div class="bottom-text">

                <div class="insight-line">

                    <span class="highlight">

                        {highest_payment_rate:.2f}%

                    </span>

                    — <b>{highest_payment_name}</b>

                    has the highest
                    payment-method churn.

                </div>


                <div class="insight-line">

                    <span class="highlight">

                        {best_cltv_value / 1000:.2f}K

                    </span>

                    — <b>{best_cltv_group}</b>

                    generates the highest
                    average CLTV.

                </div>


                <div class="insight-line">

                    Longer-tenure customers
                    provide stronger lifetime
                    value and retention
                    opportunities.

                </div>

            </div>

        </div>
        """
    )


# ============================================================
# RECOMMENDATIONS
# ============================================================

with recommendation_box:

    html(
        f"""
        <div class="bottom-card">

            <div class="bottom-heading">

                🎯 RECOMMENDATIONS

            </div>

            <div class="bottom-text">

                <div class="insight-line">

                    <b style="color:{TEAL};">

                        RETAIN

                    </b>

                    — Target vulnerable
                    high-value customers.

                </div>


                <div class="insight-line">

                    <b style="color:{TEAL};">

                        CONVERT

                    </b>

                    — Move high-risk
                    month-to-month customers
                    toward annual contracts.

                </div>


                <div class="insight-line">

                    <b style="color:{TEAL};">

                        GROW

                    </b>

                    — Use loyalty and tenure
                    incentives to increase CLTV.

                </div>

            </div>

        </div>
        """
    )
