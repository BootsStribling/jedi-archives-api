from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup as bs

def get_list(url):
  list_url = url
  res = requests.get(list_url)
  soup = bs(res.content, 'lxml')

  array = soup.find_all("a", class_="category-page__member-link")

  links = []
  for element in array:
      link = {}
      link['name'] = element.get_text()
      link['href'] = element.get('href')
      links.append(link)
  return links


def get_data():
  links = [{'name': 'The Rolling Gales', 'href': '/wiki/The_Rolling_Gales'}]
  # links = get_list(url)

  for link in links:
    href = link['href']
    page_url = f'https://starwars.fandom.com{href}'
    res = requests.get(page_url)
    soup = bs(res.content, 'lxml')
    set_data(soup)
    
    
def set_data(soup):
  # beginning the data construction
  data={}
  # image
  data['image'] = soup.find('aside', class_='portable-infobox').find('img').get('src')
  
  # name
  data['name'] = soup.find('h1', class_='page-header__title').find('i').text
  
  # description
  d_elements = soup.find('div', class_='mw-parser-output').find_all('p')
  data['description'] = []
  for element in d_elements:
    data['description'].append(element.text.strip().replace('\n', '').replace('[1]', '').replace('[2]', ''))
  data['description'].pop(0)
  data['description'].pop(0)
  data['description'].pop(0)
  n = len(data['description'])
  data['description'][0:n] = [''.join(data['description'][0:n])]
  print(data['description'])

  # infobox
  rows = soup.find('aside', class_='portable-infobox').find_all('div', class_='pi-data')
  for row in rows:
    label = row.find('h3', class_='pi-data-label').text.replace(' ', '-').replace('(s)', 's').lower()
    data[label] = []
    elements_a = row.find('div', class_='pi-data-value').find_all('a')
    values_a = []
    if(values_a):
      for value in elements_a:
        if(value.text != '[1]'):
          values_a.append(value.text)
          data[label].append(value.text)
    else:
      element_nonlink_text = row.find_all('div', class_='pi-data-value')
      for value in element_nonlink_text:
        if(value.text != '[1]'):
          data[label].append(value.text.replace('[1]', ' ').strip())
  
  print(data)

def clear_duplicates(data_object):
  for item in data_object:
    print(item, data_object[item])

get_data()