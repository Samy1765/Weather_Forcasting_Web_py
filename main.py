import streamlit as sl
import plotly.express as px
from backend import get_data
sl.set_page_config(layout="wide")

sl.header("Weather Forecasting For The Next Days")

place=sl.text_input("Place:")
days=sl.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecast days")
option=sl.selectbox("Select Data To View",("Temperature","Sky"))

sl.subheader(f"{option} for the next {days} days in {place}")

d,t=get_data(place,days,option)

figure=px.line(x=d ,y=t ,labels={"x":"Date","y":"Tempreature (C)"})
sl.plotly_chart(figure)