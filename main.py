from config import TICKERS, PERCENTAGE_CHANGE_THRESHOLD
from stockData import getPrice
import alert
import time


# Main alert loop
while(True):
    for ticker in TICKERS:
        if( getPrice(ticker)[1] >= 0):
            if getPrice(ticker)[1] >= PERCENTAGE_CHANGE_THRESHOLD: # Check daily percentage change > 10%
                message = f'🟢 {ticker} is up by {abs(getPrice(ticker)[1])}%(${getPrice(ticker)[0]}) from yesterday'
                alert.sendSMS(message)

        else:
            if getPrice(ticker)[1] <= -PERCENTAGE_CHANGE_THRESHOLD: # Check daily percentage change < -10%
                message = f'🔴 {ticker} is down by {abs(getPrice(ticker)[1])}%(${getPrice(ticker)[0]}) from yesterday'
                alert.sendSMS(message)
        time.sleep(60)