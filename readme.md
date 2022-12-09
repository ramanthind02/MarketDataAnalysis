# Market Data Analysis

From this project we use forex information obtained from calling OANDA and Poloniex APIs
to come to conclusions about market volatility and determine patterns in 
market upturns or downturns. This information can be used alongside other data sources
to analyze how global events can shape the market responses.

## Data Acquisition
- OANDA API to get information about foreign exchange values.
- Poloniex API to get information about cryptocurrency values
- Government websites to get information about bond yields

## What is the problem? What are we trying to solve?
Are the markets following a random walk? (Are the markets random?)

- Are there periods of volatility that we can measure?
- Can markets affect other markets, are there relationships between them?

## Data Analysis
- Hidden Markov Models - volatility
- Regression - market co-integration

## Requirements
- Python 3.9
- NumPy
- Pandas
- Matplotlib
- Seaborn
- hmmlearn
- plotly

## How to Run
- Requires API key from OANDA saved into `keys.py` file in `Data Collection Script` folder
  - Acquire fx-demo key. Instructions: https://developer.oanda.com/rest-live-v20/development-guide/
- Set up `keys.py` file accordingly, filling in blanks with personal OANDA account information:
    ```
    API_KEY = [INSERT API KEY HERE]
    ACCOUNT_ID = [INSERT ACCOUNT ID HERE]
    OANDA_URL = "https://api-fxpractice.oanda.com/v3"
    
    SECURE_HEADER = {
        "Authorization" : f"Bearer {API_KEY}"
    }
    ```
- Acquire data from OANDA:
  - Option 1: Run `Data Collection Script/data_collection.py` in the command line with parameters of the 
    names of the pairs (instruments). Instruments have been obtained and moved into an `instruments.pkl` file.
  - Option 2: Use the `Data Collection Script/get_currencies.ipynb` to get the currencies.
- Acquire data from Poloniex by running the `Data Collection Script/poloniex/get_crypto.ipynb` file
- Run the Jupyter scripts in the `Correlations` folder or project folder to perform statistical analyses on the data
