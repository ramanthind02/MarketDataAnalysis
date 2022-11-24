
import datetime as dt
from dateutil.parser import *


def time_utc():
    return dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)

def get_utc_dt_from_string(date_str):
    d = parse(date_str)
    return d.replace(tzinfo=dt.timezone.utc)


def get_data_filename(pair, granularity):
    return f"data/{pair}_{granularity}.pkl"

def get_instruments_filename():
    return "instruments.pkl"
