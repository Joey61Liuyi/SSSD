import pandas as pd
import yfinance as yf
import copy


data = pd.read_csv('dow_jones.csv')
for i in data.Ticker:
    stock = yf.Ticker(i)
    tep = stock.info
    # his = stock.history(period='max')
    # tep = yf.Ticker(i).history(period='max')
    print(len(tep))


# msft = yf.Ticker('AXP')
Dow30 =  []



# info = msft.info

# hist = msft.history(period = 'max')
print('pause')