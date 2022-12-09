import requests
import pandas as pd
import keys
import functions
import sys

class OandaAPI():

    def __init__(self):
        self.session = requests.Session()    

    def get_instruments(self):
        url = f"{keys.OANDA_URL}/accounts/{keys.ACCOUNT_ID}/instruments"
        response = self.session.get(url, params=None, headers=keys.SECURE_HEADER)
        return response.status_code, response.json()
    
    def get_instruments_df(self):
        code, data = self.get_instruments()
        if code == 200:
            df = pd.DataFrame.from_dict(data['instruments'])
            return df[['name', 'type', 'displayName', 'pipLocation', 'marginRate']]
        else:
            return None
    
    def save_instruments(self):
        df = self.get_instruments_df()
        if df is not None:
            df.to_pickle(functions.get_instruments_filename())

    def get_candles(self, pair_name, count=None, granularity="H1", date_from=None, date_to=None):
        url = f"{keys.OANDA_URL}/instruments/{pair_name}/candles"

        params = dict(
            granularity = granularity,
            price = "MBA"
        )
        
        if date_from is not None and date_to is not None:
            params['to'] = int(date_to.timestamp())
            params['from'] = int(date_from.timestamp())
        elif count is not None:
            params['count'] = count
        else:
            params['count'] = 300
        
        res = self.session.get(url, params=params, headers=keys.SECURE_HEADER)

        if res.status_code != 200:
            return res.status_code, None
        
        return res.status_code, res.json()


