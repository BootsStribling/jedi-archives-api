from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re

BASE_URL = 'https://starwars.fandom.com'
categories = ['/wiki/Category:Starships', 'https' ]

#*#*#*#*#*#*#*#*#*# ASSEMBLES ALL UNIQUE CATEGORY PAGES #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# def get_category():
  



#*#*#*#*#**##*#* GETS LIST OF URLS FROM WOOKIEEPEDIA CATEGORY PAGE *#*#*#*#*#*#*#*#*#*#*
def get_list(categories):
  for url in categories:
    list_url = f'{BASE_URL}{url}'
    res = requests.get(list_url)
    soup = bs(res.content, 'lxml')
    array = soup.find_all("a", class_="category-page__member-link")

    links = []
    for element in array:
        link = {}
        name = element.get_text()
        if('Category' in name or 'Starship' in name):
          pass
        else:
          link['name'] = element.get_text()
          link['href'] = element.get('href')
          links.append(link)
    urls = pd.Series(links)
    ######################TESTING ONLY - To make sure you are getting all of the URLS- Comment out When finished Testing###################
    for url in urls:
      name = url['name']
      href = url['href']
      print(f'The name is {name} and the link is {href}')
    return urls
  
get_list()


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
def create_data(soup):
  data = pd.Series()

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
