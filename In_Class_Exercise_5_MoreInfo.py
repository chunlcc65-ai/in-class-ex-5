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
    show_sector = st.checkbox(____, value=____)

    # Multiselect widget
    # fill in the code below
    # the first argument should be the label (a str), 
    # the second argument should be the S&P100 tickers, 
    # the third argument should be the default options
    selected_tickers = st.multiselect(
        ____,
        options=____,
        default=____
    )

    # Year range slider
    # fill in the code below
    # the first argument should be the label (a str), 
    # the second (third) argument should be the min (max) value, 
    # the last argument should be the default value range
    selected_years = st.slider(
        ____,
        min_value=____,
        max_value=____,
        value=(____, ____)
    )

# a bar chart that visualizes the market cap of S&P 100 stocks by sector
# fill in the code below
if show_sector:
    st.header("____")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    # the fifth argument specifies whether you want the bar chart to be horizontal.

    st.bar_chart(____, x=____, y=____, color=____, horizontal=____,
            width=720, height=500)

# display price and volme charts if stocks are selected; show error message otherwise
# fill in the code below
if selected_tickers:
    # show the header with using f-string
    st.header(f"____")
    # select the required data
    chart_data = stock_data.query(f"Date < {selected_years[1] + 1} and Date >= {selected_years[0]} and Ticker in {selected_tickers}")
 
    # Line chart for closing price
    st.subheader("Closing Prices")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    st.line_chart(____, x=____, y=____, color="Ticker",
                  width=720, height=500)

    # Bar chart for volume
    st.subheader("Trading Volume")
    # the first argument is a dataframe
    # the second, third, and fourth arguments are some columns in the dataframe
    st.bar_chart(____, x=____, y=____, color=____, 
                  width=720, height=500)

# display the error message
# fill in the code below
else:
    st.error(____)




