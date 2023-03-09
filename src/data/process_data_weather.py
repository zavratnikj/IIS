import json
import requests
import pandas as pd
import numpy as np
import pprint

MB_Titova = []
with open('data/raw/weather/neobdelani_podatki.json', 'r') as f:
    data = json.load(f)

# Extract required values from JSON data
rows = []
for item in data['list']:
    row = {
        'datetime': pd.to_datetime(item['dt'], unit='s'),
        'temp': item['main']['temp'],
        'pressure': item['main']['pressure'],
        'humidity': item['main']['humidity'],
        'wind_speed': item['wind']['speed']
    }
    rows.append(row)

# Create DataFrame from extracted values
df = pd.DataFrame(rows)

df['temp'] = df['temp'].apply(lambda x: x - 273.15)

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['time'] = df['datetime'].dt.hour

df.drop(['datetime'], axis=1, inplace=True)

df.to_csv('data/processed/weather/obdelani_podatki_weather.csv', index=False)
