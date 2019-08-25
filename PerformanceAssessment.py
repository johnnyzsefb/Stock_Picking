# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

Days = '180'
Target = '2330'
URL = 'view-source:https://histock.tw/stock/mainprofit.aspx?no=' + Target + '&day=' + Days

'''
# Start Parsing
head =head_random()
payload = {"response":'html',
            "date":date,
            "selectType":"ALLBUT0999"}
res = requests.get(URL, headers=head, params=payload)
'''
print URL