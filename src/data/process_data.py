import pandas as pd

df_air = pd.read_csv('data/processed/air/obdelani_podatki_air.csv')
df_weather = pd.read_csv('data/processed/weather/obdelani_podatki_weather.csv')

df = pd.merge(df_air, df_weather, on=['year', 'month', 'day', 'time'], how='inner')

df['year'] = df.pop('year')
df['month'] = df.pop('month')
df['day'] = df.pop('day')
df['time'] = df.pop('time')

df.to_csv('data/processed/obdelani_podatki.csv', index=False)

print(df)
