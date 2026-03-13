import requests
import json

API_KEY = "7a66476139dde1a63036f86cc47bc69f"

cities = ["Delhi", "Varanasi", "Mumbai", "aaa"]

for city in cities:

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)

    data = response.json()

    print("City:", city)
    print(json.dumps(data, indent=4))
    print("\nDetail for next city is as below")
else:
    print ("incorrect city name : ", {city})