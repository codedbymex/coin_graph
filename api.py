#!/usr/bin/env python
import argparse
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

__version__ = '0.1'
__author__ =  'Norbert Bota'
__author_email__ = 'botanorbert1@gmail.com'

parser = argparse.ArgumentParser(description='Plotting a specific coin \
                                              from coinmarketcap')

parser.add_argument('-c', '--coin',
                    action="store",
                    help='specify coin name',
                    required=True)

coin_name = parser.parse_args()
COIN = coin_name.coin

BASE_URL = "https://graphs.coinmarketcap.com/currencies/"

def get_historical_data(coin):
    r = requests.get("".join((BASE_URL, coin, "/")))
    coin_data = r.json()['price_usd']
    real_time = lambda x: datetime.fromtimestamp(x / 1e3)
    coin = {real_time(key): value for key, value in coin_data}
    return coin

def main():
    d = get_historical_data(COIN)
    df = pd.DataFrame({"Time":list(d.keys()), "Price":list(d.values())})
    df.index = df['Time']
    df['Price'].plot(figsize=(20,10), color="green")
    plt.title(COIN)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

if __name__=='__main__':
    main()
