import streamlit as st
import pandas as pd

# load stock info and data
ticker_info = pd.read_csv("ticker_info.csv")
stock_data = pd.read_csv("stock_data.csv", parse_dates=['Date'])

# extract S&P 100 tickers from ticker_info
# fill in the code below
tickers_100 = ticker_info['Ticker']

# set page title
st.title("S&P 100 Stock Dashboard 📊")  

# Sidebar controls
# fill in the code below
with st.sidebar:
    st.header("Sidebar Widgets")

    # Checkbox widget
    # fill in the code below
    # the first argument should be the label (a str), the second argument should be the default value
    show_sector = st.checkbox("Show Market Cap by Sector", value=True)

    # Multiselect widget
    # fill in the code below
    # the first argument should be the label (a str), 
    # the second argument should be the S&P100 tickers, 
    # the third argument should be the default options
    selected_tickers = st.multiselect(
        "Select Stock Tickers",
        options=tickers_100,
        default=['TSLA', 'NVDA', 'AAPL']
    )

    # Year range slider
    # fill in the code below
    # the first argument should be the label (a str), 
    # the second (third) argument should be the min (max) value, 
    # the last argument should be the default value range
    selected_years = st.slider(
        "Select Year Range",
        min_value=2020,
        max_value=2026,
        value=(2025, 2026)
    )

# a bar chart that visualizes the market cap of S&P 100 stocks by sector
# fill in the code below
if show_sector:
    st.header("Market Cap by Sector")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    # the fifth argument specifies whether you want the bar chart to be horizontal.

    st.bar_chart(ticker_info, x="Sector", y="Market Cap (B)", color="Sector", horizontal=True,
            width=720, height=500)

# display price and volme charts if stocks are selected; show error message otherwise
# fill in the code below
if selected_tickers:
    # show the header with using f-string
    st.header(f"Stock Trend Analysis (2025 - 2026)")
    # select the required data
    chart_data = stock_data.query(f"Date < {selected_years[1] + 1} and Date >= {selected_years[0]} and Ticker in {selected_tickers}")
 
    # Line chart for closing price
    st.subheader("Closing Prices")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    st.line_chart(chart_data, x="Date", y="Close", color="Ticker",
                  width=720, height=500)

    # Bar chart for volume
    st.subheader("Trading Volume")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    st.bar_chart(chart_data, x="Date", y="Volume", color="Ticker", 
                  width=720, height=500)

# display the error message
# fill in the code below
else:
    st.error("Please select at least one stock!")




