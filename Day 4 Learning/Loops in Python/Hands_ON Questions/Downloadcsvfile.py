import requests
import json
import csv

API_KEY = "7a66476139dde1a63036f86cc47bc69f"

cities = ["Delhi", "Varanasi", "Mumbai", "aaa"]
File_Data =  []

for city in cities:

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    data = response.json()

    # store fields for CSV in table in rows
    File_Data.append([city, data.get("main", {}).get("temp"), data.get("main", {}).get("humidity"), data.get("main", {}).get("speed")])

    print("City:", city)
    print(json.dumps(data, indent=4))
    print("\nDetail for next city is as below")


# create CSV AFTER loop finishes
with open("Today's weather_report.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City","Temperature","Humidity","timezone","speed"])
    writer.writerows(File_Data)

print("CSV file created")