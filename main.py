import streamlit as sl
import plotly.express as px
from backend import get_data

# frondend part
sl.set_page_config(layout="wide")

sl.header("Weather Forecasting For The Next Days")

place=sl.text_input("Place:")
days=sl.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecast days")
option=sl.selectbox("Select Data To View",("Temperature","Sky"))

sl.subheader(f"{option} for the next {days} days in {place}")

if place:
#call the imported get_data function to get the data
   try:
      filtered_data=get_data(place,days)

   

#ploting the graph for tempreature
      if option=="Temperature":
         temp=[dict["main"]["temp"]/10 for dict in filtered_data]
         dates=[dict["dt_txt"] for dict in filtered_data]
         figure=px.line(x=dates ,y=temp ,labels={"x":"Date","y":"Tempreature (C)"})
         sl.plotly_chart(figure)

      if option=="Sky":
         image={"Clear": "conditions/clear.png","Clouds": "conditions/cloud.png","Rain": "conditions/rain.png","Snow": "conditions/snow.png"}
         sky=[dict["weather"][0]["main"] for dict in filtered_data]
         image_path=[image[condition] for condition in sky]
         sl.image(image_path,width=115)
      
   except KeyError:
      sl.error("Place does not exist.")