import os
import requests
import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 53.35, "longitude": -6.26, "current_weather": True}

data = requests.get(url, params=params).json()
weather = data["current_weather"]

df = pd.DataFrame([weather])
df.to_csv("data/weather.csv", index=False)

conn = psycopg.connect(
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"),
    dbname=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
)

cur = conn.cursor()

cur.execute("""
INSERT INTO weather (time, interval, temperature, windspeed, winddirection, is_day, weathercode)
VALUES (%s,%s,%s,%s,%s,%s,%s)
""", (
    weather["time"],
    weather["interval"],
    weather["temperature"],
    weather["windspeed"],
    weather["winddirection"],
    weather["is_day"],
    weather["weathercode"]
))

conn.commit()
cur.close()
conn.close()

print("Saved to PostgreSQL")
