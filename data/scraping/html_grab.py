from bs4 import BeautifulSoup as bs
import requests
import time

BASE_URL = 'https://starwars.fandom.com'
starship_category_list = '/wiki/Special:Categories?from=Starships'

#*#*#*#*#*#*#*#*#*# ASSEMBLES ALL UNIQUE CATEGORY PAGES #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def get_categories(url_extension):
  category_url  = f'{BASE_URL}{url_extension}'
  res = requests.get(category_url)
  soup = bs(res.content, 'lxml')
  raw_category_list = soup.find('div', class_='mw-spcontent').find('ul').find_all('a')
  filtered_category_list = []
  for category in raw_category_list:
    if 'Starships' in category.text:
      filtered_category_list.append(category)
  refined_category_list = []
  for category in filtered_category_list:
    link = {}
    link['name'] = category.text
    link['href'] = category.get('href')
    refined_category_list.append(link)
  print(refined_category_list)
  return refined_category_list


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* CALLS EVERY URL IN REFINED CATEGORY LIST AND RETURNS LIST OF LINKS IN THAT CATEGORY LIST #*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#

def get_links(url_extension):
  refined_category_list = get_categories(url_extension)
  page_links = []
  print(f'{"*"* 33}Started Entire Pull at {time.strftime("%X")}{"*"* 33}')
  for link_object in refined_category_list:
    url = link_object['href']
    name = link_object['name']
    list_url = f'{BASE_URL}{url}'
    res = requests.get(list_url)
    soup = bs(res.content, 'lxml')
    print(f'{"*"* 100}')
    print(f'Started Link Call for {name} at {time.strftime("%X")}')

    links = soup.find_all("a", class_="category-page__member-link")
    for element in links:
      if 'Starship' in element.text or 'Category' in element.text:
        pass
      else:
        link = {}
        link['name'] = element.text
        link['href'] = element.get('href')
        page_links.append(link)

    print(f'Completed Link call for {name} at {time.strftime("%X")}')
    print(f'{"*"* 100}')
  print(f'{"="* 33}Completed Entire Pull at {time.strftime("%X")}{"="* 33}')
  return page_links

#*#*#*#*#*#*#*#*#*#*#*#*#* WRITES NEW HTML PAGE FOR EACH OF THE PAGE LINKS #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#*#*#*#*#* FOR PRACTICE ONLY #*#*#*#*#*#*#*#*#*#*#
def create_HTML(url_extension):
  link_objects = get_links(url_extension)
  print(f'{"*"* 33}Started HTML WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  print(f'{"*"* 100}')
  for link_object in link_objects:
    print(f'{"*"* 100}')
    name = link_object['name'].replace(' ','-').replace('/', '-')
    print(f'Started HTML write for {name} at {time.strftime("%X")}')
    url = link_object['href']
    article_url = f'{BASE_URL}{url}'
    res = requests.get(article_url)
    soup = bs(res.content, 'lxml')
    message = f'{soup}'
    f = open(f'../raw/starships/{name}.html', 'w')
    f.write(message)
    f.close()
    print(f'Completed HTML write for {name} at {time.strftime("%X")}')
    print(f'{"*"* 100}')


create_HTML(starship_category_list)



