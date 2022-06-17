from bs4 import BeautifulSoup as bs
import re
import requests
import time

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
  # Optional Loop Limiter
  # if count > 2 :
  #   return 
  count += 1
  print(f'{"*"*100}')
  print(f'List page {count} called')
  url = f'{BASE_URL}{href}'
  req = requests.get(url)
  soup = bs(req.content, 'lxml')
  elements = soup.find_all('a', title=re.compile('Special:AllPages'))
  a_tags = soup.find('ul', class_='mw-allpages-chunk').find_all('a'
  )
  get_pages(a_tags)
  print(len(a_tags), '# Of links on this page')
  print(len(pages), '<--- Cumulative Total of Pages Listed')
  unique = []
  # remove duplicates
  for element in elements:
    if element not in unique:
      if 'next' in element.text.lower(): unique.append(element)
  # gets href and name
  for element in unique:
    link = {}
    link['name'] = element.text
    link['href'] = element.get('href')
    links.append(link)
  print(links[-1]['href'], f'\n{href}', '\n ^Are these two equal? If so, you should see an END OF PAGINATION RECURSION CALL after this line.^')
  if(links[-1]['href'] == href):
    print('END OF PAGINATION RECURSION CALL')
    print('END OF PAGINATION RECURSION CALL')
    print('END OF PAGINATION RECURSION CALL')
    print('END OF PAGINATION RECURSION CALL')
    print('END OF PAGINATION RECURSION CALL')
    return
  else:
    get_next_page(links[-1]['href'], count)

#*#*#*#*#*#*#*#* WRITE NEW HTML FOR ALL PAGE LINKS #*#*#*#*#*#*#*#*#*

def capture_list_pages():
  before = time.monotonic()
  get_next_page('/wiki/Special:AllPages?from=1010+BBY', count)
  after = time.monotonic()
  print(f'Completed Page List Capture in {after - before} seconds')
  print(f'{"*"* 33}STARTED REFERENCE WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  before_html = time.monotonic()
  f = open('../scraping/list.py', 'w')
  f.write(f'links = {links}')
  f.close()
  g = open('../scraping/pages.py', 'w')
  g.write(f'pages = {pages}')
  g.close()
  after_html = time.monotonic()
  print(f'{"*"* 33}FINISHED HTML WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  print(f'FINISHED HTML WRITE IN {after_html - before_html} seconds.')
  return pages

