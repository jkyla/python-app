import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_4?keywords=sony+a7&qid=1577471091&sr=8-4'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())


import urllib2
from bs4 import BeautifulSoup
quote_page = 'https://amazon.com'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs{class': 'name'})
name = name_box.text.strip()
print(name)