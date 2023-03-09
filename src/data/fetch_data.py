import json
import requests
import pandas as pd
import numpy as np
import pprint

url = "https://arsoxmlwrapper.app.grega.xyz/api/air/archive"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    with open('data/raw/air/neobdelani_podatki.json', 'w') as f:
        json.dump(data, f)
else:
    print(f"Error: {response.status_code}")

# API_key = "facbbd327383c3c420b0a461707dc933"
# history_data = "https://api.openweathermap.org/data/2.5/history/city?lat=46.55&lon=15.65&type=hour&start=",first_date_unix,"&end=",last_date_unix,"&appid=",API_key
#
# response = requests.get(history_data)
#
# if response.status_code == 200:
#     data = json.loads(response.text)
#     pprint.pprint(data)
#     with open('../../data/raw/weather/neobdelani_podatki.json', 'w') as f:
#         json.dump(data, f)
# else:
#     print(f"Error: {response.status_code}")



