import pandas as pd
import numpy as np
import sys
import seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import re
# from statsmodels.regression.linear_model import OLS

filename_re = re.compile(r"([^/]*)\.pkl$")

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# from statsmodels.regression.linear_model import OLS

pickle_dtypes = {
    "time": np.datetime64,
    "volume": np.int64,
    "mid_o": np.float64,
    "mid_h": np.float64,
    "mid_l": np.float64,
    "mid_c": np.float64,
    "bid_o": np.float64,
    "bid_h": np.float64,
    "bid_l": np.float64,
    "bid_c": np.float64,
    "ask_o": np.float64,
    "ask_h": np.float64,
    "ask_l": np.float64,
    "ask_c": np.float64
}


def filepath_to_filename(name):
    for match in filename_re.finditer(name):
        return match.group(1)
    print("Unable to match")
    return None


def main(first_pair_loc, second_pair_loc):
    p1 = pd.read_pickle(first_pair_loc).astype(pickle_dtypes).set_index("time")
    p2 = pd.read_pickle(second_pair_loc).astype(pickle_dtypes).set_index("time")
    p1_bid = p1["bid_o"]
    p2_bid = p2["bid_o"]

    corr_res = p1_bid.corr(p2_bid)
    print(corr_res)
    scaled_p1 = p1_bid / p1_bid.max()
    scaled_p2 = p2_bid / p2_bid.max()
    plt.title("Asset Price Trends")
    plt.xlabel("Time")
    plt.ylabel("Relative Difference Compared to Max in Time Interval")
    scaled_p1.plot(label=filepath_to_filename(first_pair_loc))
    scaled_p2.plot(label=filepath_to_filename(second_pair_loc))    # scaled to 0 and 1
    plt.legend()
    plt.show()


if __name__ == "__main__":
    seaborn.set()
    main(sys.argv[1], sys.argv[2])
def main(first_pair_loc, second_pair_loc):
    p1 = pd.read_pickle(first_pair_loc).astype(pickle_dtypes).set_index("time")
    p2 = pd.read_pickle(second_pair_loc).astype(pickle_dtypes).set_index("time")
    p1_bid = p1["bid_o"]
    p2_bid = p2["bid_o"]

    corr_res = p1_bid.corr(p2_bid)
    print(corr_res)
    scaled_p1 = p1_bid / p1_bid.max()
    scaled_p2 = p2_bid / p2_bid.max()
    scaled_p1.plot()
    scaled_p2.plot()    # scaled to 0 and 1
    plt.show()
    corr_res = scaled_p1.corr(scaled_p2)
    print(corr_res)


if __name__ == "__main__":
    seaborn.set()
    main(sys.argv[1], sys.argv[2])
