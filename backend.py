import requests
#get the api and url
API_key="649775b64a4e1cbdc3e2efd1f983d5d6"

def get_data(palce, days=None):
   url=f"http://api.openweathermap.org/data/2.5/forecast?q={palce}&appid={API_key}"
   content=requests.get(url)
   data=content.json()

#filtering out the points till the days we need
   filtered_data=data["list"]
   nr_value=8*days
   filtered_data=filtered_data[:nr_value]
   return filtered_data