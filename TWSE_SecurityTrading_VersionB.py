# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import os
# import win32com.client
# import pypyodbc
import datetime
import time

def head_random():
      #for i in range(10):
      hs = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16',
            'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-tw; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)']
      hes = {"User-Agent":random.choice(hs)}
      return hes
'''
def ValidStock(date,stock_num):
      url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX'
      head =head_random()
      payload = {"response":'html',
                 "date":date,
                 "type":"ALLBUT0999"}
      res = requests.get(url, headers=head, params=payload)
      soup=BeautifulSoup(res.text, "lxml")
      #print soup
      tab = soup.select('div')
      print len(str(tab[0]))
      print str(tab[0])
      print len(str(tab))
      print str(tab)
      if len(tab[0])<=10:
            return 0
      else:
            return 1
'''
def read_network_data(date,url):
      #url = 'http://www.twse.com.tw/exchangeReport/MI_MARGN'
      head =head_random()
      payload = {"response":'html',
                 "date":date,
                 "selectType":"ALLBUT0999"}
      res = requests.get(url, headers=head, params=payload)
      #print res.url
      #print res.text
      soup=BeautifulSoup(res.text, "lxml")
      ContentLenghtCheck = soup.select('div')
      #print len(str(ContentLenghtCheck))
      #print ContentLenghtCheck
      if len(str(ContentLenghtCheck))>=3000: #3000 is empirical length number for Null data feedback
            try:
                tab_raw = soup.select('tbody')
                #print len(tab_raw)
                #print tab_raw
                tab=tab_raw[len(tab_raw)-1] # for last form
                #print tab
                #print tab.select('tr')[0].select('td')
                regs=[] # initialized the array
                for i in range(len(tab.select('tr')[0].select('td'))): #Constructing Array
                      regs.append([])
                #print len(regs)
                #print len(tab.select('tr')[0].select('td'))
                for tr in tab.select('tr'): #data fetching
                      #print tr.select('td')[0].text
                      for i in range(len(tab.select('tr')[0].select('td'))):
                            regs[i].append(tr.select('td')[i].text)
                return regs
            except:
                print '----Abnormal stop /Start printing RAW data----'
                print res.text
                print '----Abnormal stop /Stop printing RAW data----'

      else:
            print 'no such date for this stock!'
            return 0
'''
read_network_data('20170603')
read_network_data('20170604')
read_network_data('20170605')

#Main script starts from here
StartDate=raw_input('請輸入開始擷取日期(西元日期如：2016/1/1)：')
EndDate=raw_input('請輸入結束擷取日期(西元日期如：2016/1/31)：')
#Date transforming
ts=time.time()
StartDate = time.strptime(str(StartDate), "%Y/%m/%d")
EndDate =time.strptime(EndDate, "%Y/%m/%d")
StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
EndDate =  datetime.date(EndDate[0], EndDate[1], EndDate[2])
RangeDate = datetime.timedelta(days = 1)
print StartDate
print EndDate

print(time.strftime('%a %H:%M:%S'))
re=read_network_data('20170601',1)

print re[0]
print(time.strftime('%a %H:%M:%S'))
print re[6]
print(time.strftime('%a %H:%M:%S'))

while StartDate <= EndDate:
      yy,mm,dd=str(StartDate).split('-')
      dat=datetime.datetime(int(yy), int(mm), int(dd))
      dd=dat.strftime('%Y/%m/%d')
      year=str(int(dd[0:4])-1911)
      date=dd.replace(dd[0:4], year)
      print('目前執行網路擷取',date ,'日的資料，請稍後...')
      re=read_network_data(date,1)
      if re[0][0]=='查無資料':
            print(date,'日，可能為休市日，查無資料。')
            StartDate = StartDate + RangeDate
            continue
'''
