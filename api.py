#!/usr/bin/env python
import sys
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

__version__ = '0.1'
__author__ =  'Norbert Bota'
__author_email__= 'botanorbert1@gmail.com'

# Plotting a specific coin from coinmarketcap
if sys.argv[1] == '-c':
	COIN = str(sys.argv[2])
elif "-c" not in sys.argv[0:2]:
	exit("Usage: api.py -c <coin> \nexample: api.py -c bitcoin")
	
BASE_URL = "https://graphs.coinmarketcap.com/currencies/"

def get_historical_data(coin):
	r = requests.get("".join((BASE_URL, coin, "/")))
	coin_data = r.json()['price_usd']
	result = {}
	
	for i in coin_data:
		real_time = i[0] / 1e3
		temp = datetime.fromtimestamp(real_time) #.strftime('%Y-%m-%d %H:%M:%S')
		new_coin = {temp:i[1]}
		result.update(new_coin)
	return result

def main():
	d = get_historical_data(COIN)
	df = pd.DataFrame({"Time": d.keys(), "Price": d.values()})
	df.index = df['Time']
	df['Price'].plot(figsize=(20,10), color="green")
 	plt.title(COIN)
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.show()

if __name__=='__main__':
	main()
