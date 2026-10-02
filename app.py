"""
CodeAlpha Python Programming Internship - Task 02
Stock Portfolio Tracker - Streamlit Dashboard
Theme: Premium Clean Light Theme (Soft Off-White + Coral Red + Soft Pink)
"""

import pandas as pd
import streamlit as st
import altair as alt

# Predefined sample stock prices (sample data, not live market prices)
PREDEFINED_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 420.0,
    "AMZN": 185.0,
    "NVDA": 120.0,
    "META": 500.0,
}

# Streamlit Page Configuration
st.set_page_config(
    page_title="Stock Portfolio Tracker | CodeAlpha Task 02",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Clean, Light Theme
st.markdown(
    """
    <style>
    /* Main App Background & Base Typography */
    .stApp {
        background-color: #F8F7FA !important;
        color: #24212B !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }

    /* Light Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E8E4EB !important;
    }
    [data-testid="stSidebar"] * {
        color: #24212B !important;
    }

    /* Header Container */
    .header-container {
        padding: 5px 0 20px 0;
        border-bottom: 1px solid #E8E4EB;
        margin-bottom: 25px;
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #24212B;
        letter-spacing: -0.5px;
        margin: 0;
    }
    .main-title span {
        color: #E85D75;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #77717F;
        margin-top: 4px;
        font-weight: 400;
    }

    /* Summary Metric Cards */
    .card-highlight {
        background-color: #FCE7F3;
        border: 1px solid #F4A6C1;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 4px 15px rgba(232, 93, 117, 0.08);
        transition: transform 0.2s ease;
    }
    .card-highlight:hover {
        transform: translateY(-2px);
    }
    .card-white {
        background-color: #FFFFFF;
        border: 1px solid #E8E4EB;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 4px 15px rgba(36, 33, 43, 0.04);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .card-white:hover {
        transform: translateY(-2px);
        border-color: #F4A6C1;
    }

    .metric-label {
        font-size: 0.85rem;
        color: #77717F;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-val-coral {
        font-size: 2.1rem;
        font-weight: 800;
        color: #E85D75;
        margin: 0;
    }
    .metric-val-dark {
        font-size: 2.1rem;
        font-weight: 800;
        color: #24212B;
        margin: 0;
    }
    .metric-pill {
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 600;
        background: #FFFFFF;
        color: #E85D75;
        padding: 4px 10px;
        border-radius: 20px;
        margin-top: 8px;
        border: 1px solid #F4A6C1;
    }
    .metric-pill-gray {
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 600;
        background: #F8F7FA;
        color: #77717F;
        padding: 4px 10px;
        border-radius: 20px;
        margin-top: 8px;
        border: 1px solid #E8E4EB;
    }

    /* Section Containers */
    .section-box {
        background-color: #FFFFFF;
        border: 1px solid #E8E4EB;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 4px 15px rgba(36, 33, 43, 0.03);
    }
    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #24212B;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .accent-pill {
        width: 6px;
        height: 18px;
        background-color: #E85D75;
        border-radius: 3px;
        display: inline-block;
    }

    /* Primary Coral Red Buttons */
    .stButton>button {
        background-color: #E85D75 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.2rem !important;
        box-shadow: 0 3px 8px rgba(232, 93, 117, 0.25) !important;
        transition: background-color 0.2s ease, transform 0.1s ease !important;
    }
    .stButton>button:hover {
        background-color: #d14960 !important;
        transform: translateY(-1px) !important;
    }

    /* Download CSV Button */
    .stDownloadButton>button {
        background-color: #FFFFFF !important;
        color: #E85D75 !important;
        border: 1.5px solid #E85D75 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.2rem !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
    }
    .stDownloadButton>button:hover {
        background-color: #FCE7F3 !important;
        border-color: #E85D75 !important;
        color: #E85D75 !important;
    }

    /* Sidebar Form */
    [data-testid="stForm"] {
        background-color: #F8F7FA !important;
        border: 1px solid #E8E4EB !important;
        border-radius: 12px !important;
        padding: 16px !important;
    }

    /* Footer */
    .footer-note {
        text-align: center;
        color: #77717F;
        font-size: 0.85rem;
        margin-top: 35px;
        padding-top: 15px;
        border-top: 1px solid #E8E4EB;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- HEADER -----------------
st.markdown(
    """
    <div class="header-container">
        <h1 class="main-title">Stock Portfolio <span>Tracker</span></h1>
        <div class="sub-title">Track your investments with ease • CodeAlpha Python Programming Internship – Task 02</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {
        "AAPL": {"quantity": 10, "price": 180.0, "investment_value": 1800.0},
        "TSLA": {"quantity": 5, "price": 250.0, "investment_value": 1250.0},
        "GOOGL": {"quantity": 8, "price": 150.0, "investment_value": 1200.0},
    }

portfolio_data = st.session_state.portfolio

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding-bottom: 10px;">
            <h3 style="color: #24212B; font-size: 1.25rem; font-weight: 700; margin: 0;">
                💼 Manage Holdings
            </h3>
            <p style="color: #77717F; font-size: 0.85rem; margin-top: 4px;">
                Add or modify stock positions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form(key="add_stock_form", clear_on_submit=False):
        selected_symbol = st.selectbox(
            "Select Stock Symbol:",
            options=list(PREDEFINED_PRICES.keys()),
            index=0,
            help="Choose from predefined sample stock tickers.",
        )

        quantity_input = st.number_input(
            "Quantity of Shares:",
            min_value=1,
            max_value=100000,
            value=10,
            step=1,
            help="Enter a positive integer representing number of shares.",
        )

        submitted = st.form_submit_button("➕ Add to Portfolio", use_container_width=True)

        if submitted:
            if quantity_input <= 0:
                st.error("❌ Quantity must be greater than 0.")
            else:
                price = PREDEFINED_PRICES[selected_symbol]
                investment_val = quantity_input * price

                st.session_state.portfolio[selected_symbol] = {
                    "quantity": quantity_input,
                    "price": price,
                    "investment_value": investment_val,
                }
                st.success(f"✅ Added {quantity_input} shares of {selected_symbol}!")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <h4 style="color: #24212B; font-size: 0.95rem; font-weight: 700; margin-bottom: 8px;">
            📋 Predefined Sample Prices
        </h4>
        """,
        unsafe_allow_html=True,
    )
    price_df = pd.DataFrame(
        [{"Symbol": k, "Sample Price ($)": f"${v:.2f}"} for k, v in PREDEFINED_PRICES.items()]
    )
    st.dataframe(price_df, use_container_width=True, hide_index=True)

    if st.button("🔄 Reset Portfolio", use_container_width=True):
        st.session_state.portfolio = {}
        st.rerun()


# ----------------- SUMMARY CARDS -----------------
if portfolio_data:
    total_investment = sum(item["investment_value"] for item in portfolio_data.values())
    total_shares = sum(item["quantity"] for item in portfolio_data.values())
    num_symbols = len(portfolio_data)
else:
    total_investment = 0.0
    total_shares = 0
    num_symbols = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="card-highlight">
            <div class="metric-label">Total Portfolio Investment</div>
            <div class="metric-val-coral">${total_investment:,.2f}</div>
            <div class="metric-pill">● Portfolio Value</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="card-white">
            <div class="metric-label">Total Stocks Held</div>
            <div class="metric-val-dark">{total_shares:,} <span style="font-size: 1.1rem; font-weight: 500; color: #77717F;">shares</span></div>
            <div class="metric-pill-gray">● Total Volume</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="card-white">
            <div class="metric-label">Different Stock Symbols</div>
            <div class="metric-val-dark">{num_symbols} <span style="font-size: 1.1rem; font-weight: 500; color: #77717F;">symbols</span></div>
            <div class="metric-pill-gray">● Diversification</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- MAIN HOLDINGS & VISUALIZATION -----------------
if portfolio_data:
    display_rows = []
    for sym, details in portfolio_data.items():
        display_rows.append(
            {
                "Stock Symbol": sym,
                "Quantity": details["quantity"],
                "Predefined Price ($)": details["price"],
                "Total Value ($)": details["investment_value"],
            }
        )
    df_portfolio = pd.DataFrame(display_rows)

    col_table, col_chart = st.columns([1.05, 1.15])

    with col_table:
        st.markdown(
            '<div class="section-title"><span class="accent-pill"></span> Stock Holdings Table</div>',
            unsafe_allow_html=True,
        )

        formatted_df = df_portfolio.copy()
        formatted_df["Predefined Price ($)"] = formatted_df["Predefined Price ($)"].apply(
            lambda x: f"${x:,.2f}"
        )
        formatted_df["Total Value ($)"] = formatted_df["Total Value ($)"].apply(
            lambda x: f"${x:,.2f}"
        )

        st.dataframe(formatted_df, use_container_width=True, hide_index=True)

        csv_data = df_portfolio.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Portfolio as CSV",
            data=csv_data,
            file_name="stock_portfolio.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col_chart:
        st.markdown(
            '<div class="section-title"><span class="accent-pill" style="background-color: #F4A6C1;"></span> Investment Value by Stock</div>',
            unsafe_allow_html=True,
        )

        # Altair bar chart with Coral Red and Soft Pink theme palette
        chart = (
            alt.Chart(df_portfolio)
            .mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8)
            .encode(
                x=alt.X(
                    "Stock Symbol:N",
                    title="Stock Symbol",
                    axis=alt.Axis(
                        labelColor="#24212B",
                        titleColor="#24212B",
                        labelFontWeight="bold",
                        grid=False,
                    ),
                ),
                y=alt.Y(
                    "Total Value ($):Q",
                    title="Investment Value ($)",
                    axis=alt.Axis(
                        labelColor="#77717F",
                        titleColor="#77717F",
                        gridColor="#E8E4EB",
                    ),
                ),
                color=alt.Color(
                    "Stock Symbol:N",
                    scale=alt.Scale(
                        range=["#E85D75", "#F4A6C1", "#F9C6D6", "#D14960", "#FCE7F3"]
                    ),
                    legend=None,
                ),
                tooltip=[
                    alt.Tooltip("Stock Symbol:N", title="Symbol"),
                    alt.Tooltip("Quantity:Q", title="Shares"),
                    alt.Tooltip("Predefined Price ($):Q", title="Price ($)", format="$.2f"),
                    alt.Tooltip("Total Value ($):Q", title="Total Value ($)", format="$.2f"),
                ],
            )
            .properties(height=320, background="transparent")
            .configure_view(strokeWidth=0)
        )

        st.altair_chart(chart, use_container_width=True)

else:
    st.info("💡 Your portfolio is currently empty. Use the sidebar on the left to add stock holdings.")

# ----------------- FOOTER -----------------
st.markdown(
    """
    <div class="footer-note">
        ⚠️ <strong>Note:</strong> Stock prices are manually predefined sample values for CodeAlpha Internship Task 02 and do not represent real-time financial market data.
    </div>
    """,
    unsafe_allow_html=True,
)
