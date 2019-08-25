import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
from itertools import chain

url = "http://www.foxrun.com.au/Products/Cylinders_with_Gadgets.aspx"

def validate(soup):
    return {"__VIEWSTATE": soup.select_one("#__VIEWSTATE")["value"],
            "__VIEWSTATEGENERATOR": soup.select_one("#__VIEWSTATEGENERATOR")["value"],
            "__EVENTVALIDATION": soup.select_one("#__EVENTVALIDATION")["value"]}

def parse(base, url):
    data = {"__ASYNCPOST": "true"
            }
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17'}
    soup = BeautifulSoup(requests.get(url).text)
    data.update(validate(soup))
    # gets links for < 1,2,3,4,5,6>
    pages = [a["id"] for a in soup.select("a[id^=ctl01_ctl00_pbsc1_pbPagerBottom_btnP]")][2:]
    # get images from initial page
    yield [img["src"] for img in soup.select("img")]
    # add token for post 
    data.update(validate(soup))
    for p in pages:
        # we need $ in place of _ for the form data
        data["__EVENTTARGET"] = p.replace("_", "$")
        data["RadScriptManager1"] = "ctl01$ctl00$pbsc1$ctl01$ctl00$pbsc1$ajaxPanel1Panel|{}".format(p.replace("_", "$"))
        r = requests.post(url, data=data, headers=h).text
        soup = BeautifulSoup(r)
        yield [urljoin(base, img["src"]) for img in soup.select("img")]


for url in chain.from_iterable(parse("http://www.foxrun.com.au/", url)):
    print(url)