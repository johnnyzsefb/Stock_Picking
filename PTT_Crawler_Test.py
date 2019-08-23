import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/stock/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print response.text
articles = soup.find_all('div', 'r-ent')
#print articles
# not sure if this will afect?
for article in articles:
    try:
        meta = article.find('div', 'title').find('a')
        title = meta.getText().strip()
        link = meta.get('href')
        push = article.find('div', 'nrec').getText()
        date = article.find('div', 'date').getText()
        author = article.find('div', 'author').getText()
    
        print(push, title, date, author)  # result of setp-3
    except:
        continue