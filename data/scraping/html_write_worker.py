from bs4 import BeautifulSoup as bs
import requests
import time


BASE_URL = 'https://starwars.fandom.com'
links = [] #for each of the list pagination links
pages = [] # for each of the links on the list pages- the links to all wookieepedia pages themselves
count = 0
# Calls page_ref which opens pages.py to find the pages list and set it equal to the total variable
total = page_ref()
# Divides  total into 3 sections
divisor1 = round(len(total)/3)
divisor2 = divisor1 * 2
divisor3 = len(total) - 1
page_section1 = total[0:divisor1]
page_section2 = total[divisor1:divisor2]
page_section3 = total[divisor2:divisor3]
print(len(total), '<----- Length of Total Pages')
print(len(page_section1), '<------ Length of Page Section 1')
print(len(page_section2), '<------ Length of Page Section 2')
print(len(page_section3), '<------ Length of Page Section 3')

#*#*#*#*#*#*#*#* WRITE NEW HTML FOR ALL PAGE LINKS #*#*#*#*#*#*#*#*#*

def write_HTML_worker(section):
  print(f'{"*"* 33}Started HTML WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  print(f'{"*"* 100}')
  before = time.monotonic()
  for page in section:
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
  after = time.monotonic()
  print(f'{"*"* 33}COMPLETED HTML WRITING PROCESS at {time.strftime("%X")}{"*"* 33}')
  print(f'COMPLETED HTML WRITING PROCESS IN {after - before} seconds.')


#Testing Call- do not uncomment unless you want this to run twice!
# write_HTML_1()
