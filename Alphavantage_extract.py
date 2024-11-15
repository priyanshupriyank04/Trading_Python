from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time   //import these libraries for usage

key = "your_api_key_here"

ts = TimeSeries(key=key,output_format='pandas')  
data = ts.get_daily(symbol="EURUSD",outputsize='full')[0]    #create data which stores sample forex EURUSD OHLCV data
data.columns = ["open","high","low","close","volume"]

data = data.iloc[::-1]  #reversing data extracted from alpha_vantage since it gives you reverse data of Yfinance

#extracting multiple stock datas

all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG","FB"]    #choose any stock of your choice 
close_prices = pd.DataFrame()
api_call_count = 0                          #api count to keep track of 5 api calls/min restriction of alpha_vantage
start_time = time.time()                    #keep hold of time to be used for sleep function 

for ticker in all_tickers:
    ts = TimeSeries(key=key,output_format='pandas')
    data = ts.get_intraday(symbol=ticker,interval='1min',outputsize='compact')[0]  
    api_call_count+=1                    #increment api count 
    data.columns = ["open","high","low","close","volume"]    
    close_prices[ticker] = data["close"]
    if api_call_count==5:        #when api count reaches 5 reset count to 0 and use time.sleep() to pause code for remainder of the minute restriction left
        api_call_count = 0;
        time.sleep(60 - (time.time()-start_time)%60)
