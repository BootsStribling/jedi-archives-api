from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re

BASE_URL = 'https://starwars.fandom.com'
start_href = '/wiki/Special:AllPages?from=%2224-karat%22+beaches'
pages = []

def crawl(url):
  page= {}
  res = requests.get(url)
  soup = bs(res.content, 'lxml')
  next_pgtxt = soup.find('div', class_='mw-allpages-nav').find('a').text.lower()
  next_pghref = soup.find('div', class_='mw-allpages-nav').find('a').get('href')
  if('next' in next_pgtxt):
    page['txt'] = next_pgtxt
    page['href'] = next_pghref
    pages.append(page)
    next_page = f'{BASE_URL}{next_pghref}'
    crawl(next_page)

crawl(f'{BASE_URL}{start_href}')


print(pages)


