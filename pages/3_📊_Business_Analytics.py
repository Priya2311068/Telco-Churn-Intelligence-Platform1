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

BG = "#F7F9FC"
CARD = "#FFFFFF"
CARD_2 = "#F1F5F9"
BORDER = "#D7E2EC"

CYAN = "#168CE3"
TEAL = "#145B8F"
PURPLE = "#6D28D9"
ORANGE = "#E0525E"
GREEN = "#2A9D8F"

TEXT = "#16324F"
MUTED = "#64748B"

# ============================================================
# CONSISTENT VISUAL FONT SIZES
# ============================================================

DATA_LABEL_SIZE = 11.5
AXIS_LABEL_SIZE = 9.5
AXIS_TITLE_SIZE = 10
CHART_TITLE_SIZE = 12.5
CATEGORY_LABEL_SIZE = 10


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
    }}


    /* ======================================================
       SECTION TITLE
    ====================================================== */

    .section-title {{
        color: {TEXT};
        font-size: 12.5px;
        font-weight: 800;
        margin-top: 4px;
        margin-bottom: 3px;
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
        box-shadow: 0 5px 14px rgba(15,47,79,.08);
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
                rgba(67,212,224,.23),
                rgba(147,100,231,.20)
            );
    }}

    .kpi-value {{
        font-size: 18px;
        font-weight: 850;
        color: {TEXT};
        margin-top: 5px;
        line-height: 1;
    }}

    .kpi-label {{
        font-size: 8.8px;
        color: {MUTED};
        margin-top: 5px;
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
        box-shadow: 0 4px 12px rgba(15,47,79,.07);

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

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #F8FBFE
            );

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
       LIGHT THEME CONSISTENCY OVERRIDES
    ====================================================== */

    html, body, [data-testid="stAppViewContainer"] {
        background: #F7F9FC !important;
        color: #16324F !important;
    }

    section[data-testid="stSidebar"] * {
        color: #16324F !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    div[data-baseweb="select"] > div {
        background: #FFFFFF !important;
        color: #16324F !important;
        border: 1px solid #C9D6E2 !important;
    }

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] svg {
        color: #16324F !important;
        fill: #64748B !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"],
    li[role="option"] {
        background: #FFFFFF !important;
        color: #16324F !important;
    }

    li[role="option"]:hover {
        background: #EAF5FD !important;
        color: #145B8F !important;
    }

    .hero, .kpi, .recommend,
    div[data-testid="stPlotlyChart"] {
        color: #16324F !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

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
    "TotalCharges",
    "Total Charges"
])

contract_col = find_column([
    "Contract"
])

internet_col = find_column([
    "InternetService",
    "Internet Service"
])

payment_col = find_column([
    "PaymentMethod",
    "Payment Method"
])

gender_col = find_column([
    "Gender",
    "gender"
])

security_col = find_column([
    "OnlineSecurity",
    "Online Security"
])

reason_col = find_column([
    "Churn Reason",
    "ChurnReason"
])


# ============================================================
# NUMERIC CLEANING
# ============================================================

for col in [
    tenure_col,
    monthly_col,
    total_col
]:

    if col:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )


# ============================================================
# CREATE CHURN FLAG
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

    return values.isin([
        "yes",
        "churned",
        "1",
        "true"
    ]).astype(int)


df["Churn_Flag"] = create_churn_flag(df)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🔎 Filters")

st.sidebar.caption(
    "Explore customer churn interactively."
)


filtered_df = df.copy()


def add_filter(data, column, label):

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

    choice = st.sidebar.selectbox(
        label,
        ["All"] + options
    )

    if choice != "All":

        data = data[
            data[column]
            .astype(str)
            .eq(choice)
        ]

    return data


filtered_df = add_filter(
    filtered_df,
    internet_col,
    "📡 Internet Service"
)

filtered_df = add_filter(
    filtered_df,
    contract_col,
    "📄 Contract"
)

filtered_df = add_filter(
    filtered_df,
    payment_col,
    "💳 Payment Method"
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
    """
    <div class="hero">

        <div class="hero-icon">
            📡
        </div>

        <div>

            <div class="hero-title">

                Telco

                <span style="color:#168CE3;">
                    Customer
                </span>

                <span style="color:#E0525E;">
                    Churn
                </span>

                <span style="color:#6D28D9;">
                    Analytics
                </span>

            </div>

            <div class="hero-subtitle">
                CUSTOMER RETENTION • REVENUE RISK • CHURN DRIVERS • BUSINESS INTELLIGENCE
            </div>

        </div>

    </div>
    """
)


# ============================================================
# KPI VALUES
# ============================================================

total_customers = len(filtered_df)

churned_customers = int(
    filtered_df["Churn_Flag"].sum()
)


churn_rate = (
    churned_customers
    / total_customers
    * 100
    if total_customers > 0
    else 0
)


if monthly_col:

    monthly_loss = (
        filtered_df.loc[
            filtered_df["Churn_Flag"] == 1,
            monthly_col
        ]
        .fillna(0)
        .sum()
    )

else:

    monthly_loss = 0


if total_col:

    total_loss = (
        filtered_df.loc[
            filtered_df["Churn_Flag"] == 1,
            total_col
        ]
        .fillna(0)
        .sum()
    )

else:

    total_loss = 0


if tenure_col:

    avg_tenure = (
        filtered_df[
            tenure_col
        ]
        .dropna()
        .mean()
    )

else:

    avg_tenure = 0


# ============================================================
# KPI FUNCTION
# ============================================================

def kpi(icon, value, label):

    html(
        f"""
        <div class="kpi">

            <div class="kpi-icon">
                {icon}
            </div>

            <div class="kpi-value">
                {value}
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
    '<div class="section-title">📌 Executive Overview</div>'
)


k1, k2, k3, k4, k5, k6 = st.columns(
    6,
    gap="small"
)


with k1:
    kpi(
        "👥",
        f"{total_customers:,}",
        "Total Customers"
    )


with k2:
    kpi(
        "🚪",
        f"{churned_customers:,}",
        "Churned Customers"
    )


with k3:
    kpi(
        "📉",
        f"{churn_rate:.2f}%",
        "Churn Rate"
    )


with k4:
    kpi(
        "💸",
        f"{monthly_loss / 1000:.2f}K",
        "Monthly Revenue Lost"
    )


with k5:
    kpi(
        "💰",
        f"{total_loss / 1_000_000:.2f}M",
        "Total Revenue Lost"
    )


with k6:
    kpi(
        "⏳",
        f"{avg_tenure:.2f}",
        "Avg Tenure Months"
    )


# ============================================================
# STANDARD CHART STYLE
# ============================================================

def style_chart(
    fig,
    title,
    height=188,
    x_title="",
    y_title="",
    show_x_labels=True,
    show_y_labels=False
):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.02,

            font=dict(
                size=CHART_TITLE_SIZE,
                color=TEXT
            )
        ),

        height=height,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        # SAME VISUAL PADDING
        margin=dict(
            l=42,
            r=32,
            t=42,
            b=36
        ),

        font=dict(
            family="Arial",
            color=TEXT,
            size=9.2
        ),

        bargap=0.12,

        showlegend=False,

        hoverlabel=dict(
            bgcolor=CARD_2,
            font_color=TEXT,
            font_size=11
        ),

        # Helps prevent Plotly shrinking trace text
        uniformtext=dict(
            minsize=DATA_LABEL_SIZE,
            mode="show"
        )
    )


    fig.update_xaxes(

        title=x_title,

        showgrid=False,
        zeroline=False,

        showticklabels=show_x_labels,

        color=MUTED,

        tickfont=dict(
            size=AXIS_LABEL_SIZE
        ),

        title_font=dict(
            size=AXIS_TITLE_SIZE,
            color=MUTED
        )
    )


    fig.update_yaxes(

        title=y_title,

        showgrid=False,
        zeroline=False,

        showticklabels=show_y_labels,

        color=MUTED,

        tickfont=dict(
            size=AXIS_LABEL_SIZE
        ),

        title_font=dict(
            size=AXIS_TITLE_SIZE,
            color=MUTED
        )
    )


    return fig


# ============================================================
# CHURN DRIVERS
# ============================================================

html(
    '<div class="section-title">📊 Churn Drivers</div>'
)


internet_box, tenure_box, contract_box = st.columns(
    [0.72, 1.62, 0.72],
    gap="medium"
)


# ============================================================
# INTERNET SERVICE
# ============================================================

with internet_box:

    if internet_col:

        internet_data = (
            filtered_df
            .groupby(
                internet_col,
                dropna=False
            )["Churn_Flag"]
            .mean()
            .mul(100)
            .reset_index()
        )


        internet_data.columns = [
            internet_col,
            "rate"
        ]


        internet_data = (
            internet_data
            .sort_values(
                "rate",
                ascending=False
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=internet_data[
                internet_col
            ],

            y=internet_data[
                "rate"
            ],

            width=0.38,

            marker_color=CYAN,

            text=[
                f"{v:.1f}%"
                for v in internet_data[
                    "rate"
                ]
            ],

            textposition="outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>%{x}</b>"
                "<br>"
                "Churn Rate: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        fig = style_chart(
            fig,
            "📡 Internet Service",
            height=188,
            x_title="Internet Service",
            y_title="Churn Rate (%)",
            show_x_labels=True,
            show_y_labels=False
        )


        fig.update_xaxes(
            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
                color=TEXT
            )
        )


        fig.update_yaxes(

            range=[
                0,
                max(
                    55,
                    internet_data[
                        "rate"
                    ].max() * 1.22
                )
            ]
        )


        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "displayModeBar": False
            }
        )


# ============================================================
# TENURE LINE CHART
# ============================================================

with tenure_box:

    if tenure_col:

        tenure_data = (
            filtered_df
            .dropna(
                subset=[tenure_col]
            )
            .groupby(
                tenure_col
            )["Churn_Flag"]
            .mean()
            .mul(100)
            .reset_index()
            .sort_values(
                tenure_col
            )
        )


        target_points = [
            12,
            24,
            36,
            48,
            60,
            72
        ]


        labels = []
        positions = []


        for _, row in tenure_data.iterrows():

            month = int(
                row[tenure_col]
            )

            if month in target_points:

                labels.append(
                    f"{row['Churn_Flag']:.1f}%"
                )

                if month in [
                    12,
                    36,
                    60
                ]:

                    positions.append(
                        "bottom center"
                    )

                else:

                    positions.append(
                        "top center"
                    )

            else:

                labels.append("")
                positions.append(
                    "top center"
                )


        max_idx = (
            tenure_data[
                "Churn_Flag"
            ].idxmax()
        )


        peak_row = (
            tenure_data.loc[
                max_idx
            ]
        )


        peak_month = float(
            peak_row[
                tenure_col
            ]
        )


        peak_rate = float(
            peak_row[
                "Churn_Flag"
            ]
        )


        fig = go.Figure()


        fig.add_trace(

            go.Scatter(

                x=tenure_data[
                    tenure_col
                ],

                y=tenure_data[
                    "Churn_Flag"
                ],

                mode="lines+markers+text",

                line=dict(
                    color=PURPLE,
                    width=2.2
                ),

                marker=dict(
                    size=3.6,
                    color=PURPLE
                ),

                text=labels,

                textposition=positions,

                textfont=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT
                ),

                fill="tozeroy",

                fillcolor="rgba(147,100,231,.10)",

                hovertemplate=(
                    "<b>"
                    "Tenure: %{x} months"
                    "</b>"
                    "<br>"
                    "Churn Rate: %{y:.2f}%"
                    "<extra></extra>"
                )
            )
        )


        # Peak value uses SAME LABEL SIZE
        fig.add_trace(

            go.Scatter(

                x=[peak_month],

                y=[peak_rate],

                mode="markers+text",

                marker=dict(
                    size=7,
                    color=PURPLE
                ),

                text=[
                    f"{peak_rate:.1f}%"
                ],

                textposition="top center",

                textfont=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT
                ),

                hovertemplate=(
                    "<b>Highest Churn Rate</b>"
                    "<br>"
                    f"Tenure: {int(peak_month)} month"
                    "<br>"
                    f"Churn Rate: {peak_rate:.2f}%"
                    "<extra></extra>"
                ),

                showlegend=False
            )
        )


        fig = style_chart(
            fig,
            (
                "📉 Churn Risk Declines "
                "as Customer Tenure Increases"
            ),
            height=188,
            x_title="Tenure (Months)",
            y_title="Churn Rate (%)",
            show_x_labels=True,
            show_y_labels=False
        )


        fig.update_yaxes(

            range=[
                0,
                max(
                    78,
                    peak_rate * 1.25
                )
            ]
        )


        fig.update_xaxes(

            tickmode="array",

            tickvals=[
                0,
                12,
                24,
                36,
                48,
                60,
                72
            ],

            ticktext=[
                "0",
                "12",
                "24",
                "36",
                "48",
                "60",
                "72"
            ],

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
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
# CONTRACT
# ============================================================

with contract_box:

    if contract_col:

        contract_data = (
            filtered_df
            .groupby(
                contract_col,
                dropna=False
            )["Churn_Flag"]
            .mean()
            .mul(100)
            .reset_index()
        )


        contract_data.columns = [
            contract_col,
            "rate"
        ]


        contract_data = (
            contract_data
            .sort_values(
                "rate"
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=contract_data[
                "rate"
            ],

            y=contract_data[
                contract_col
            ],

            orientation="h",

            width=0.38,

            marker_color=CYAN,

            text=[
                f"{v:.1f}%"
                for v in contract_data[
                    "rate"
                ]
            ],

            textposition="outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>"
                "Churn Rate: %{x:.2f}%"
                "<extra></extra>"
            )
        )


        fig = style_chart(
            fig,
            "📄 Contract",
            height=188,
            x_title="Churn Rate (%)",
            show_x_labels=False,
            show_y_labels=True
        )


        max_contract_rate = (
            contract_data[
                "rate"
            ].max()
        )


        fig.update_xaxes(

            range=[
                0,
                max_contract_rate * 1.24
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
                "displayModeBar": False
            }
        )


# ============================================================
# GAP
# ============================================================

html(
    '<div class="row-gap"></div>'
)


# ============================================================
# SECOND VISUAL ROW
# ============================================================

cohort_box, reasons_box, security_box, charges_box = st.columns(
    [
        0.82,
        1.34,
        0.88,
        0.88
    ],
    gap="medium"
)


# ============================================================
# TENURE COHORT
# ============================================================

with cohort_box:

    if tenure_col:

        temp = filtered_df.copy()


        temp[
            "Tenure Cohort"
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
                "0–12",
                "13–24",
                "25–48",
                "49+"
            ]
        )


        cohort_data = (
            temp
            .groupby(
                "Tenure Cohort",
                observed=False
            )["Churn_Flag"]
            .mean()
            .mul(100)
            .reset_index()
        )


        fig = go.Figure()


        # Bars do NOT use trace text
        fig.add_bar(

            x=cohort_data[
                "Tenure Cohort"
            ],

            y=cohort_data[
                "Churn_Flag"
            ],

            width=0.38,

            marker_color=ORANGE,

            hovertemplate=(
                "<b>%{x} months</b>"
                "<br>"
                "Churn Rate: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        # Fixed annotations with SAME DATA LABEL SIZE
        for _, row in cohort_data.iterrows():

            fig.add_annotation(

                x=row[
                    "Tenure Cohort"
                ],

                y=row[
                    "Churn_Flag"
                ] + 2.1,

                text=(
                    f"<b>"
                    f"{row['Churn_Flag']:.1f}%"
                    f"</b>"
                ),

                showarrow=False,

                font=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT,
                    family="Arial"
                ),

                xanchor="center",

                yanchor="bottom"
            )


        fig = style_chart(
            fig,
            "⏳ Churn by Tenure Cohort",
            height=190,
            x_title="Tenure (Months)",
            y_title="Churn Rate (%)",
            show_x_labels=True,
            show_y_labels=False
        )


        cohort_max = (
            cohort_data[
                "Churn_Flag"
            ].max()
        )


        fig.update_yaxes(

            range=[
                0,
                max(
                    64,
                    cohort_max * 1.32
                )
            ]
        )


        fig.update_xaxes(

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
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
# TOP 5 CHURN REASONS
# ============================================================

with reasons_box:

    if reason_col:

        churn_reasons = (
            filtered_df[
                filtered_df[
                    "Churn_Flag"
                ] == 1
            ][reason_col]
            .dropna()
            .astype(str)
            .value_counts()
            .head(5)
        )


        def clean_reason(reason):

            replacements = {

                "Attitude of support person":
                    "Support staff attitude",

                "Competitor offered higher download speeds":
                    "Higher competitor speed",

                "Competitor offered more data":
                    "Competitor offered more data",

                "Competitor made better offer":
                    "Better competitor offer",

                "Attitude of service provider":
                    "Service provider attitude",

                "Don't know":
                    "Don't know"
            }

            return replacements.get(
                reason,
                reason
            )


        reason_df = pd.DataFrame({

            "display_reason": [
                clean_reason(x)
                for x in churn_reasons.index
            ],

            "count":
                churn_reasons.values
        })


        reason_df = (
            reason_df
            .sort_values(
                "count",
                ascending=True
            )
        )


        fig = go.Figure()


        fig.add_bar(

            x=reason_df[
                "count"
            ],

            y=reason_df[
                "display_reason"
            ],

            orientation="h",

            width=0.38,

            marker_color=CYAN,

            hovertemplate=(
                "<b>%{y}</b>"
                "<br>"
                "Churned Customers: %{x}"
                "<extra></extra>"
            )
        )


        max_reason = (
            reason_df[
                "count"
            ].max()
        )


        # Fixed annotations using SAME DATA LABEL SIZE
        for _, row in reason_df.iterrows():

            fig.add_annotation(

                x=row[
                    "count"
                ] + (
                    max_reason * 0.018
                ),

                y=row[
                    "display_reason"
                ],

                text=(
                    f"<b>"
                    f"{int(row['count'])}"
                    f"</b>"
                ),

                showarrow=False,

                font=dict(
                    size=DATA_LABEL_SIZE,
                    color=TEXT,
                    family="Arial"
                ),

                xanchor="left",

                yanchor="middle"
            )


        fig = style_chart(
            fig,
            "🎯 Top 5 Churn Reasons",
            height=190,
            x_title="Churned Customers",
            show_x_labels=False,
            show_y_labels=True
        )


        fig.update_xaxes(

            range=[
                0,
                max_reason * 1.18
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
                "displayModeBar": False
            }
        )


# ============================================================
# ONLINE SECURITY
# ============================================================

with security_box:

    if security_col:

        security_data = (
            filtered_df
            .groupby(
                security_col,
                dropna=False
            )["Churn_Flag"]
            .mean()
            .mul(100)
            .reset_index()
        )


        security_data.columns = [
            security_col,
            "rate"
        ]


        fig = go.Figure()


        fig.add_bar(

            x=security_data[
                security_col
            ],

            y=security_data[
                "rate"
            ],

            width=0.38,

            marker_color=PURPLE,

            text=[
                f"{v:.1f}%"
                for v in security_data[
                    "rate"
                ]
            ],

            textposition="outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>%{x}</b>"
                "<br>"
                "Churn Rate: %{y:.2f}%"
                "<extra></extra>"
            )
        )


        fig = style_chart(
            fig,
            "🔐 Online Security",
            height=190,
            x_title="",
            y_title="Churn Rate (%)",
            show_x_labels=True,
            show_y_labels=False
        )


        fig.update_xaxes(

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
                color=TEXT
            )
        )


        fig.update_yaxes(

            range=[
                0,
                max(
                    55,
                    security_data[
                        "rate"
                    ].max() * 1.22
                )
            ]
        )


        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "displayModeBar": False
            }
        )


# ============================================================
# AVG MONTHLY CHARGES
# ============================================================

with charges_box:

    if monthly_col:

        charge_data = (
            filtered_df
            .groupby(
                "Churn_Flag"
            )[monthly_col]
            .mean()
            .reset_index()
        )


        charge_data[
            "Status"
        ] = (
            charge_data[
                "Churn_Flag"
            ]
            .map({
                0: "Retained",
                1: "Churned"
            })
        )


        fig = go.Figure()


        fig.add_bar(

            x=charge_data[
                "Status"
            ],

            y=charge_data[
                monthly_col
            ],

            width=0.38,

            marker_color=[
                TEAL,
                ORANGE
            ][:len(
                charge_data
            )],

            text=[
                f"${v:.2f}"
                for v in charge_data[
                    monthly_col
                ]
            ],

            textposition="outside",

            textfont=dict(
                size=DATA_LABEL_SIZE,
                color=TEXT
            ),

            cliponaxis=False,

            hovertemplate=(
                "<b>%{x}</b>"
                "<br>"
                "Average Monthly Charges: $%{y:.2f}"
                "<extra></extra>"
            )
        )


        fig = style_chart(
            fig,
            "💳 Avg Monthly Charges",
            height=190,
            x_title="Customer Status",
            y_title="Avg Monthly Charges",
            show_x_labels=True,
            show_y_labels=False
        )


        fig.update_xaxes(

            tickfont=dict(
                size=CATEGORY_LABEL_SIZE,
                color=TEXT
            )
        )


        fig.update_yaxes(

            range=[
                0,
                max(
                    95,
                    charge_data[
                        monthly_col
                    ].max() * 1.20
                )
            ]
        )


        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "displayModeBar": False
            }
        )


# ============================================================
# GAP BEFORE RECOMMENDATIONS
# ============================================================

# 7px instead of the global 10px gap:
# moves only the recommendation section upward by 3px.
html(
    '<div style="height:7px;"></div>'
)


# ============================================================
# RECOMMENDATIONS
# ============================================================

html(
    '<div class="section-title">💡 Recommended Actions</div>'
)


r1, r2, r3, r4 = st.columns(
    4,
    gap="medium"
)


def recommendation(title, text):

    html(
        f"""
        <div class="recommend">

            <div class="recommend-title">
                {title}
            </div>

            <div class="recommend-text">
                {text}
            </div>

        </div>
        """
    )


with r1:

    recommendation(
        "🎯 RETAIN",
        (
            "Target month-to-month customers "
            "with attractive contract-conversion incentives."
        )
    )


with r2:

    recommendation(
        "🛡️ PROTECT",
        (
            "Promote Online Security and resolve "
            "service issues among high-risk customers."
        )
    )


with r3:

    recommendation(
        "🤝 ENGAGE",
        (
            "Prioritise proactive retention campaigns "
            "during each customer's first 12 months."
        )
    )


with r4:

    recommendation(
        "🔄 CONVERT",
        (
            "Move high-risk customers toward one-year "
            "or two-year contracts with targeted offers."
        )
    )
