#!/usr/bin/env python3

import requests
from pprint import pprint

# 1. get an api key, and use a different company (MSFT)
url = 'https://www.'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=2SnXduIBPDy9UnlWKOrxkKL_U0ZfmK45'
r = requests.get(url)
data = r.json()

lowlist= []
high_list= []

# looping over all time dictionaries
for x in data["Time Series (15min)"]:
    # from each dictionary, get the low value "3. low"
    lowlist.append(data["Time Series (5min)"][x]["3. low"])

# also return the highest stock value <-- "2. high"
# looping over all time dictionaries
for y in data["Time Series (15min)"]:
    high_list.append(data["Timeseries (15min)"][y]"2. high"])
print(min(lowlist))
print(max(high_list))

# to show the percentae change of highest and lowest price 
if lenght(lowlist) == length(high_list):
    for i in len(lowlist): 
        print(f'{(high_list[i]}  {low_list[i]}  {(((lowlist[i] - high_list[i]) / lowlist) * 100))}')  
