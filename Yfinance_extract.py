#This is the sample code to simply extract data of stocks from Yfinance 


import datetime as dt          #datetime used for date and time functions
import yfinance as yf          #used to extract stock OHLC data 
import pandas as pd            #for creating dataframes 

stocks = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]    #enter all stock data you want to extract data for 
start = dt.datetime.today() - dt.timedelta(60)              #start date is assigned by calculating difference between today's date and 60 days before date using timedelta function
end = dt.datetime.today()          #end date is assigned as today's date using datetime.tdday() function 
cl_price = pd.DataFrame()        #create a dataframe using pandas for storing the data 

ohlc = {}      #create empty dictionary for storing 
for ticker in stocks:      #for loop to iterate over stocks array one by one 
    ohlc[ticker] = yf.download(ticker,start,end)    #use yf.download alias to download stock data from start to end date and assign it to ticker in the dictionary where ticker represents the stock name 
