from bs4 import BeautifulSoup
from htmlgen import htmlgen

import requests
from bs4 import BeautifulSoup

def get_list():
  list_url = 'https://starwars.fandom.com/wiki/Category:starships'
  res = requests.get(list_url)
  soup = BeautifulSoup(res.content, 'lxml')

  array = soup.find_all("a", class_="category-page__member-link")

  links = []
  for element in array:
      link = {}
      link['name'] = element.get_text()
      link['href'] = element.get('href')
      links.append(link)
  return links


def get_html():
  links = [{'name': 'Ravenstar', 'href': '/wiki/Ravenstar'}]
  # links = get_list()

  for link in links:
    href = link['href']
    page_url = f'https://starwars.fandom.com{href}'
    res = requests.get(page_url)
    soup = BeautifulSoup(res.content, 'lxml')
    
    data={}
    data['image'] = soup.find('aside', class_='portable-infobox').find('img').get('src')
    label_length = len(soup.find_all('h3', class_='pi-data-label'))
    for i in range(label_length):
      label_parent = soup.find('aside', class_='portable-infobox').find('h3', class_='pi-data-label')
      label = soup.find('aside', class_='portable-infobox').find('div').find('a').string
      for j in 
      label_parent.decompose()
      
      print(parent.decomposed, '<-if the parent was destroyed')



    print('data', data)
    

get_html()