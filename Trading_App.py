import streamlit as st
st.set_page_config(
    page_title="Trading App",
    page_icon="charts_with_downward_trend",
    layout="wide"
)

st.title("Trading Guide App :bar_chart:")
st.header("We provide a platform to help you invest in stocks.")
st.image("app.jpg")
st.markdown("## We provide the following services:")

st.markdown("#### :one: Stock Information")
st.write("Through this page,you can see all the information about stock.")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models.Use this tool to gain valuable insights into the market trends and make informed investment decisions.")