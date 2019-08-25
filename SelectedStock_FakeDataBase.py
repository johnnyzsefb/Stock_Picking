import requests
URL='http://goodinfo.tw/StockInfo/StockDividendSchedule.asp?STOCK_ID=3056'
s=requests.Session()
r=s.get(URL)
