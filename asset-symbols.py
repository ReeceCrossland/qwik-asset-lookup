#!/usr/bin/env python3

import requests
import pandas as pd
import os

from api_keyz import api_key

api_url = 'https://finnhub.io/api/v1/'
symbols_root_dir = 'symbols'
asset_types = ['crypto', 'forex']


def exchange_lists(type):
    response = requests.get(api_url + type + '/exchange?token=' + api_key)
    response_json = response.json()
    return response_json


def csv_dir(asset_type):
    os.makedirs(os.path.join(symbols_root_dir, asset_type), exist_ok=True)


def symbols_csv(type, exchange):
    response = requests.get(api_url + type + '/symbol?exchange=' + exchange + '&token=' + api_key)
    response_json = response.json()
    dataframe = pd.DataFrame(response_json)
    pd.DataFrame(dataframe).to_csv(os.path.join(symbols_root_dir, asset_type, type + '_' + exchange + '.csv'))


for asset_type in asset_types:
    csv_dir(asset_type)
    for exchange in exchange_lists(asset_type):
        symbols_csv(asset_type, exchange)

