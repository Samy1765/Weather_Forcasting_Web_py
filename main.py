import streamlit as sl

sl.set_page_config(layout="wide")
sl.header("Weather Forecasting For The Next Days")
place=sl.text_input("Place:")
days=sl.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecast days")
option=sl.selectbox("Select Data To View",("Temperature","Sky"))

sl.subheader(f"{option} for the next {days} days in {place}")