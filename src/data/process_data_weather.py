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
        'wind_speed': item['wind']['speed'],
        'weather_main': item['weather'][0]['main'],
        'weather_description': item['weather'][0]['description']
    }
    rows.append(row)

# Create DataFrame from extracted values
df = pd.DataFrame(rows)

df['temp'] = df['temp'].apply(lambda x: x - 273.15)

weather_main_dummies = pd.get_dummies(df['weather_main'], prefix='weather_main')
weather_description_dummies = pd.get_dummies(df['weather_description'], prefix='weather_description')

# Concatenate the dummy variables with the original dataframe
df = pd.concat([df, weather_main_dummies, weather_description_dummies], axis=1)

# Drop the original weather_main and weather_description columns
df = df.drop(['weather_main', 'weather_description'], axis=1)

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['time'] = df['datetime'].dt.hour

df.drop(['datetime'], axis=1, inplace=True)

df.to_csv('data/processed/weather/obdelani_podatki_weather.csv', index=False)
