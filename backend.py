import requests

API_key="56bd1180b9b3408845dbcb00d1913b81"
def get_data(palce, days, type):
   url=f"http:api.openweathermap.org/data/2.5/forecast?q={palce}&appid={API_key}"
   coontent=requests.get(url)
   data=coontent.json()
   return data