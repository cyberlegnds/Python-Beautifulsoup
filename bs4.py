from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

site = 'https://news.google.com/rss?hl=de&gl=AT&ceid=AT:de'
op = urlopen(site)
rd = op.read()
op.close()
sp_page = soup(rd, 'xml')
news_list = sp_page.find_all('item')
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print('-' * 60)