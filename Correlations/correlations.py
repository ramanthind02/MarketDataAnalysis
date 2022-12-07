import pandas as pd
import numpy as np
import sys
import seaborn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import re
# from statsmodels.regression.linear_model import OLS

filename_re = re.compile(r"([^/]*)\.pkl$")

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


def get_pickle_df_bid_o(file):
    df = pd.read_pickle(file).astype(pickle_dtypes).set_index("time")
    df = df["bid_o"]
    return df


def corr_two_files(first_pair_loc, second_pair_loc, output_file_name=None):
    first_pair_fn = filepath_to_filename(first_pair_loc)
    second_pair_fn = filepath_to_filename(second_pair_loc)
    p1_bid = get_pickle_df_bid_o(first_pair_loc).rename(first_pair_fn)
    p2_bid = get_pickle_df_bid_o(second_pair_loc).rename(second_pair_fn)

    # join on time to get rid of missing fields
    joined = pd.concat([p1_bid, p2_bid], axis=1).dropna()
    p1_bid = joined[first_pair_fn]
    p2_bid = joined[second_pair_fn]

    corr_res = p1_bid.corr(p2_bid)
    print(corr_res)
    scaled_p1 = p1_bid / p1_bid.max()
    scaled_p2 = p2_bid / p2_bid.max()
    scaled_p1.plot()
    scaled_p2.plot()  # scaled to 0 and 1
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Relative Value To Max Value")
    plt.title("Relation Between Two Pairs")
    if output_file_name is None:
        plt.show()
    else:
        plt.savefig(fname=output_file_name + ".png", format="png")


def main(first_pair_loc, second_pair_loc):
    corr_two_files(first_pair_loc, second_pair_loc)


if __name__ == "__main__":
    seaborn.set()
    main(sys.argv[1], sys.argv[2])
