import streamlit as st
import yfinance as yf
import datetime

st.write("""
             # Stock Price Analyser """)

# get data for Apple's stock
symbol = st.selectbox("Symbol", ("AAPL", "GOOG", "TSLA", "MSFT", "NFLX"))
# symbol = "AAPL"

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input("End Date", datetime.date(2023, 7, 30))

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(
    period="1d", start=start_date, end=end_date)

st.write(f"""
    ### {symbol}'s Stock price data
""")

st.dataframe(ticker_df)

st.write("""
    ### Apple's Closing Price chart
         """)

st.line_chart(ticker_df["Close"])
