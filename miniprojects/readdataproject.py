#!/usr/bin/env python3

import requests
from pprint import pprint

# 1. get an api key, and use a different company (MSFT)
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=2SnXduIBPDy9UnlWKOrxkKL_U0ZfmK45'
r = requests.get(url)
data = r.json()

lowlist= []
high_list= []

# looping over all time dictionaries
for x in data["Time Series (15min)"]:
    # from each dictionary, get the low value "3. low"
    lowlist.append(data["Time Series (15min)"][x]["3. low"])

# also return the highest stock value <-- "2. high"
# looping over all time dictionaries
for y in data["Time Series (15min)"]:
    high_list.append(data["Time Series (15min)"][y]["2. high"])

# save those values as a variable
smallest= min(lowlist)
highest= max(high_list)

print(smallest)
print(highest)

# to show the percentae change of highest and lowest price 


if len(lowlist) == len(high_list):
    for i in range(0, len(lowlist)): 
        #print(lowlist)
        #print(high_list)
        x= float( high_list[i]) - float(lowlist[i])
        y= x / float(lowlist[i]) # tito needs to fix this cause chad is dumb :(
        y= round(y * 100, 2)
        print(f"{high_list[i]}  {lowlist[i]}  {y}%")  




