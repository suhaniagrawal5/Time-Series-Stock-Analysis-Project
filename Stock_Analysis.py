import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta
from pages.utils.plotly_figure import plotly_table

#setting page config

st.set_page_config(
    page_title="Stock Analysis",
    page_icon="page_with_curl",
    layout="wide"
)
st.title("Stock Analysis")

col1,col2,col3 =st.columns(3)
today=datetime.date.today()
with col1:
    ticker=st.text_input("Stock Ticker","TSLA")
with col2:
    start_date=st.date_input("Choose Start Date", datetime.date(today.year -1,today.month,today.day))
with col3:
    end_date=st.date_input("Choose End Date", datetime.date(today.year,today.month,today.day))

st.subheader(ticker)
stock = yf.Ticker(ticker)
st.write(stock.info['longBusinessSummary'])
st.write("**Sector:**",stock.info['sector'])
st.write("**Full Time Employees:**",stock.info['fullTimeEmployees'])
st.write("**Website:**",stock.info['website'])

col1,col2 = st.columns(2)
with col1:
    df=pd.DataFrame(index=['market Cap','Beta','EPS','PE Ratio'])
    df['']=[stock.info["marketCap"],stock.info["beta"],stock.info["trailingEps"],stock.info["trailingPE"]]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df,use_container_width=True)
with col2:
    df = pd.DataFrame(index=['Quick Ratio','Revenue per share','Profit Margins','Debt to Equity','Return On Equity'])
    df['']=[stock.info["quickRatio"],stock.info["revenuePerShare"],stock.info["profitMargins"],stock.info["debtToEquity"],stock.info["returnOnEquity"]]
    fig_df=plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

# data=yf.download(ticker,start=start_date,end=end_date)

# col1,col2,col3 =st.columns(3)
# daily_change=data['Close'].iloc[-1] - data['Close'].iloc[-2]
# col1.metric("Daily Change",str(round(data['Close'].iloc[-1],2)),str(round(daily_change,2)))

