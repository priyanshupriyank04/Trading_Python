#This is sample code to be used for just automated web opening of the specified stock on Yfinance and also extracting the stock financial data




from selenium import webdriver  #does all the web scraping automation 
from selenium.webdriver.common.by import By   #import By class from selenium module 


path = "your_chrome_driver_path_here"   #write the path of the chromer diver into it where you have placed the chrome driver on your system
service = webdriver.chrome.service.Service(path)    #add the service to automate opening of chrome browser 
service.start()         #this initiates opening the browser 

ticker = "AAPL"         #write the stock name you want to scrape 

#create empty url to mimic the financial of yfinance
#add ticker in the placeholder in the provided url structure 
url = "https://finance.yahoo.com/quote/{}/financials?p={}".format(ticker, ticker)

driver = webdriver.Chrome(service=service)  #use it to open the url 
driver.get(url)                 #gets the url we created
driver.implicitly_wait(2)       #use the implicit wait function to ensure that browser is allowed to load even in poor connection conditions 

table = driver.find_element(By.XPATH,"//div[@class='tableBody yf-1pgoo1f']").text  #this table stores all the content of the stock we wanted to enquire using this 
print(table)
