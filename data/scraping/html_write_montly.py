# find('div', class_='page').find('main', class_='page__main').find('div', class_='page-content').find('div', class_='mw-body-content')
#*#*#*#*#**##*#* GETS LIST OF URLS FROM WOOKIEEPEDIA CATEGORY PAGE *#*#*#*#*#*#*#*#*#*#*
# def get_list(categories):
#   for url in categories:
#     list_url = f'{BASE_URL}{url}'
#     res = requests.get(list_url)
#     soup = bs(res.content, 'lxml')
#     array = soup.find_all("a", class_="category-page__member-link")

#     links = []
#     for element in array:
#         link = {}
#         name = element.get_text()
#         if('Category' in name or 'Starship' in name):
#           pass
#         else:
#           link['name'] = element.get_text()
#           link['href'] = element.get('href')
#           links.append(link)
#     urls = pd.Series(links)
#     ######################TESTING ONLY - To make sure you are getting all of the URLS- Comment out When finished Testing###################
#     for url in urls:
#       name = url['name']
#       href = url['href']
#       print(f'The name is {name} and the link is {href}')
#     return urls
  
# get_list()


#*#*#*#*#*#*#*#*#*#*##*# REQUESTS HTML AND RETURNS SOUP TREE #*#*#*#*#*#*#*#*#*#*#*
# def request_data():
#   urls = [{'name': 'The Millenium Falcon', 'href': '/wiki/Millennium_Falcon'}]
# #   # links = get_list(url)
#   for url in urls:
#     href = url['href']
#     page = f'{BASE_URL}{href}'
#     res = requests.get(page)
#     soup = bs(res.content, 'lxml')
#   return soup


#*#*#*#*#*#*#*#*#*#*#*# CREATES DATA OBJECT SERIES USING PANDAS BASED ON MongoDB MODEL #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# def create_data(soup):
#   data = pd.Series()
#   print(data)

# create_data()
#   for link in links:
#     href = link['href']
#     page_url = f'https://starwars.fandom.com{href}'
#     res = requests.get(page_url)
#     soup = bs(res.content, 'lxml')
#     data = set_data(soup)
#     return data
    
    
# def set_data(soup):
#   # beginning the data construction
#   data={}
#   # image
#   data['image'] = soup.find('aside', class_='portable-infobox').find('img').get('src')
  
#   # name
#   data['name'] = soup.find('h1', class_='page-header__title').find('i').text
  
#   # description
#   d_elements = soup.find('div', class_='mw-parser-output').find_all('p')
#   data['description'] = []
#   for element in d_elements:
#     data['description'].append(element.text.strip().replace('\n', '').replace('[1]', '').replace('[2]', ''))

#   data['description'].pop(0)
#   data['description'].pop(0)
#   data['description'].pop(0)
#   n = len(data['description'])
#   data['description'][0:n] = [''.join(data['description'][0:n])]
#   if(len(data['description']) == 1):
#     data['description'] = data['description'][0]

#   # infobox
#   rows = soup.find('aside', class_='portable-infobox').find_all('div', class_='pi-data')
#   for row in rows:
#     label = row.find('h3', class_='pi-data-label').text.replace(' ', '-').replace('(s)', 's').lower()
#     data[label] = []
#     elements_a = row.find('div', class_='pi-data-value').find_all('a')
#     values_a = []
#     for value in elements_a:
#       if(value.text != '[1]'):
#         values_a.append(value.text)
#         data[label].append(value.text)
#     if(len(values_a) < 1):
#       element_nonlink_text = row.find_all('div', class_='pi-data-value')
#       for value in element_nonlink_text:
#         if(value.text != '[1]'):
#           data[label].append(value.text.replace('[1]', ' ').strip())
#   return data

# links = pd.Series(links)

# data = get_data()
# ship = pd.Series(data)
# print(ship.image)
# ship.image = 'special test'
# print(ship.image)
import asyncio
from bs4 import BeautifulSoup as bs
import re
import requests
import time
import os

BASE_URL = 'https://starwars.fandom.com'
links = [] #for each of the list pagination links
pages = [] # for each of the links on the list pages- the links to all wookieepedia pages themselves
count = 0
#*#*#*#*#*#*#*#*#* GETS ALL A TAG PAGE LINKS IN LIST PAGE
  
def get_pages(a_tags):
  for a in a_tags:
    page = {}
    page['name'] = a.text
    page['href'] = a.get('href')
    pages.append(page)

#*#*#*#*#*#*GET NEXT PAGE FROM WOOKIEEPEDIA LIST #*#*#*#*#*#*#**#*#*#*#*#*#*

def get_next_page(href, count):
  url = f'{BASE_URL}{href}'
  req = requests.get(url)
  soup = bs(req.content, 'lxml')
  elements = soup.find_all('a', title=re.compile('Special:AllPages'))
  a_tags = soup.find('ul', class_='mw-allpages-chunk').find_all('a'
  )
  get_pages(a_tags)
  unique = []
  # remove duplicates
  for element in elements:
    if(element not in unique): unique.append(element)
  # gets href and name
  for element in unique:
    link = {}
    link['name'] = element.text
    link['href'] = element.get('href')
    links.append(link)
  count += 1
  print(f'List page {count} called \n{"*"*100}')
  if(links[-1]['href'] == href):
    return
  else:
    if(count <= 900):
      get_next_page(links[-1]['href'], count)

#*#*#*#*#*#*#*#* WRITE NEW HTML FOR ALL PAGE LINKS #*#*#*#*#*#*#*#*#*

def write_HTML(pages):
  get_next_page('/wiki/Special:AllPages?from=1010+BBY', count)
  print(f'{"*"* 33}Started HTML WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  print(f'{"*"* 100}')
  for page in pages:
    print(f'{"*"* 100}')
    name = page['name'].replace(' ','-').replace('/', '-')
    print(f'Started HTML write for {name} at {time.strftime("%X")}')
    url = page['href']
    page_url = f'{BASE_URL}{url}'
    res = requests.get(page_url)
    soup = bs(res.content, 'lxml')
    message = f'{soup}'
    f = open(f'../raw/a-z/{name}.html', 'w')
    f.write(message)
    f.close()
    print(f'Completed HTML write for {name} at {time.strftime("%X")}')
    print(f'{"*"* 100}')

write_HTML(pages)