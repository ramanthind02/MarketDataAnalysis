import datetime
import json

import numpy as np
import pandas as pd
import requests


def get_urls(start_epoch, end_epoch, pair_name):
    curr_start = start_epoch
    one_day = 86400
    ret = []
    # can only do 500 results
    while curr_start < end_epoch:
        temp_end = min(end_epoch, curr_start + (one_day * 300))
        url = f"https://poloniex.com/public?command=returnChartData&" \
              f"currencyPair={pair_name}" \
              f"&start={curr_start}" \
              f"&end={temp_end}" \
              f"&period=86400"
        ret.append(url)
        curr_start = temp_end
    return ret

def get_crypto(pair_name):
    # from 2016 to 2021 since USDT came out in 2014
    urls = get_urls(int(datetime.datetime(2016, 1, 1, 0, 0, 0).strftime("%s")),
                    int(datetime.datetime(2021, 12, 31, 23, 59, 59).strftime("%s")), pair_name)
    # 5 years from 2016 to 2021

    df = None
    for url in urls:
        req = requests.get(url)
        json_resp = json.loads(req.text)
        if df is None:
            df = pd.json_normalize(json_resp)
        else:
            df = pd.concat([df, pd.json_normalize(json_resp)])

    df = df.astype({
        "high": np.float64,
        "low": np.float64,
        "open": np.float64,
        "close": np.float64,
        "volume": np.float64,
        "quoteVolume": np.float64,
        "weightedAverage": np.float64
    })

    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df = df.drop_duplicates(subset=["date"])
    df = df.set_index("date")
    return df
