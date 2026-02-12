import requests
import pandas as pd
import sqlite3

# API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 53.35,
    "longitude": -6.26,
    "current_weather": True
}

response = requests.get(url, params=params)
data = response.json()
weather = data["current_weather"]

# CSV
df = pd.DataFrame([weather])
df.to_csv("data/weather.csv", index=False)

# SQL база
conn = sqlite3.connect("data/weather.db")

df.to_sql("weather", conn, if_exists="append", index=False)

conn.close()

print("Saved to CSV and SQL database")
