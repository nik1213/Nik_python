import requests
import json

API_KEY = "7a66476139dde1a63036f86cc47bc69f"

# take cities from user
cities = input("Enter city names separated by comma: ").split(",")

for city in cities:

    city = city.strip()   # remove extra spaces

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)

    data = response.json()

    print("City:", city)
    print(json.dumps(data, indent=4))
    print("\nDetail for next city is as below")

else:
    print("Incorrect city name:", city)