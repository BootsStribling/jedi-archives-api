from bs4 import BeautifulSoup
import requests
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


def get_data(url):
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
    # setting image url on data
    data['image'] = soup.find('aside', class_='portable-infobox').find('img').get('src')
    rows = soup.find('aside', class_='portable-infobox').find_all('div', class_='pi-data')
    row_length = len(rows)
    for row in rows:
      print(type(rows[row].Tag))
      
    #   label = bs(rows[row], 'lxml').find('h3', class_='pi-data-label').string
    #   print(label)
    #   # print('row', rows[row])
    #   print('<---------------------------------------------->')
      # row_soup = bs(row, 'lxml')
      # print(row_soup)
    
    
      # parent = soup.find('div', class_='pi-data')
      # label = soup.find('aside', class_ ='portable-infobox').find('h3', class_='pi-data-label').get_text(strip=True)
      # value_length = len(soup.find_all('div', class_='pi-data-value'))
      # label = label.replace(')','').replace('(','').replace(' ', '-').lower()
      # data[label] = []
      # values = soup.find('div', class_='pi-data-value').find_all('a')
      #   data[label] = value

        
      #   value = soup.find('aside', class_='portable-infobox').find('div').find('a').string
      # parent.decompose()
      
      # print(parent.decomposed, '<-if the parent was destroyed')



    print('data', data)    

get_data()