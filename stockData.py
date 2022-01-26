from config import YAHOO_API_KEY
import requests

headers = {
    'x-api-key': YAHOO_API_KEY
}

# Query the API for price data
def getPrice(ticker):
    URL = f'https://yfapi.net/v8/finance/chart/{ticker}' # Request URL

    # query parameters
    query = { 
    'comparisons': [ticker,'USD'],
    'range': '2d',
    'interval': '1d',
}
    # Make the request
    try:
        response = requests.get(URL, params=query, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        response = None

    # Get closing prices 
    if(response is not None and response.json()['chart']['result'] is not None):
        data = response.json()['chart']['result'][0]['indicators']['quote'][0]['close']
    else:
        data = None

    # Price change data
    if data is not None and data[1] is not None:
        daily_price_change = round(abs(data[1] - data[0]), 2)
        daily_percentage_change = round(((data[1] - data[0]) / data[0] * 100), 2)
    else:
        daily_price_change = 0
        daily_percentage_change = 0

    return daily_price_change, daily_percentage_change