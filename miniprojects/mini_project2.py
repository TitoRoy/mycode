#!/usr/bin/env python3

import requests
import pandas as pd

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

#print(data)
df = pd.DataFrame(data)
description = df.describe()

print(df)

#print(data["Time Series (5min)"]["2022-08-10 19:15:00"])
#print(df.describe())
