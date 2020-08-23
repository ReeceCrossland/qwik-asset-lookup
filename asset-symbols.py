#!/usr/bin/env python3

import requests
import pandas as pd
import os

from api_keyz import api_key

api_url = 'https://finnhub.io/api/v1/'
symbols_dir = 'symbols_csv'
asset_types = ['crypto', 'forex']


def exchangelists(type):
    response = requests.get(api_url + type + '/exchange?token=' + api_key)
    response_json = response.json()
    return response_json


def csvdir(asset_type):
    os.makedirs(os.path.join(symbols_dir, asset_type), exist_ok=True)

def symbolscsv(type, exchange):
    response = requests.get(api_url + type + '/symbol?exchange=' + exchange + '&token=' + api_key)
    response_json = response.json()
    dataframe = pd.DataFrame(response_json)
    pd.DataFrame(dataframe).to_csv(os.path.join(symbols_dir, asset_type, type + '_' + exchange + '_symbols.csv'))

for asset_type in asset_types:
    csvdir(asset_type)
    for exchange in exchangelists(asset_type):
        symbolscsv(asset_type, exchange)