import pandas as pd

df_air = pd.read_csv('../../data/processed/air/obdelani_podatki_air.csv')
df_weather = pd.read_csv('../../data/processed/weather/obdelani_podatki_weather.csv')

# df_air['datetime'] = pd.to_datetime(df_air[['year', 'month', 'day', 'time']])
# df_weather['datetime'] = pd.to_datetime(df_weather[['year', 'month', 'day', 'time']])
print(df_air.iloc[6]['time'])
