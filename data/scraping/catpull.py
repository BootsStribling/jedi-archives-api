from bs4 import BeautifulSoup as bs
import pandas as pd
import asyncio
import aiohttp
import random
import time
import requests
import re

BASE_URL = 'https://starwars.fandom.com'
start_href = '/wiki/Special:AllPages?from=%2224-karat%22+beaches'
pages = []


####################################################################################
# async def main():
#   print('hello')
#   await asyncio.sleep(1)
#   print('world!')

# asyncio.run(main())


####################################################################################
async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)

# async def main():
#   print(f'started at {time.strftime("%X")}')

#   await say_after(1, 'hello')
#   await say_after(2, 'world')

#   print(f'finished at {time.strftime("%X")}')

# asyncio.run(main())
####################################################################################

# async def main():
#   task1 = asyncio.create_task(
#     say_after(1, 'hello')
#   )
#   task2 = asyncio.create_task(
#     say_after(2, 'world')
#   )

#   print(f'started at {time.strftime("%X")}')

#   await task1
#   await task2

#   print(f'finished at {time.strftime("%X")}')

# asyncio.run(main())
####################################################################################

# async def nested():
#   return 42

# async def main():

#   print(await nested())

# asyncio.run(main())

####################################################################################
##FUTURES

# async def main():
#   await asyncio.gather(
#     function_that_returns_a_future_object(),
#     some_python_coroutine()
#   )

####################################################################################
##RUNNING TASKS CONCURRENTLY

# async def factorial(name, number):
#   f = 1
#   for i in range(2, number + 1):
#     print(f'Task {name}: Compute factorial({number}), currently i={i}...')
#     await asyncio.sleep(1)
#     f *= i
#   print(f'Task {name}: factorial({number}) = {f}')
#   return f

# async def main():
#   L = await asyncio.gather(
#     factorial("A", 2,),
#     factorial("B", 3,),
#     factorial("C", 4,),
#   )
#   print(L)

# asyncio.run(main())
####################################################################################
##SHIELDING FROM CANCELLATION

# try:
#     res = await shield(something())
# except CancelledError:
#     res = None

####################################################################################
##TIMEOUTS

# async def eternity():
#   await asyncio.sleep(3600)
#   print('yay!')

# async def main():
#   try:
#     await asyncio.wait_for(eternity(), timeout=1.0)
#   except asyncio.TimeoutError:
#     print('timeout!')

# asyncio.run(main())

####################################################################################
##QUEUES

async def worker(name, queue):
  while True:
    # Get a "work item" out of the queue.
    sleep_for = await queue.get()
    # Sleep for the "sleep_for" seconds.
    await asyncio.sleep(sleep_for)
    #  Notify the queue that the "work item" has been processed.
    queue.task_done()

    print(f'{name} has slept for {sleep_for:.2f} seconds')

async def main():
  # Create a queue that we will use to store our "workload".
  queue = asyncio.Queue()

  # Generate random timings and put them into the queue.
  total_sleep_time = 0
  for _ in range(20):
    sleep_for = random.uniform(0.05, 5.0)
    total_sleep_time += sleep_for
    queue.put_nowait(sleep_for)

  # Create three worker tasks to process the queue concurrently.
  tasks = []
  for i in range(3):
    task = asyncio.create_task(worker(f'worker-{i}', queue))
    tasks.append(task)

  # Wait until the queue is fully processed.
  started_at = time.monotonic()
  await queue.join()
  total_slept_for = time.monotonic() - started_at

  # Cancel our worker tasks.
  for task in tasks:
    task.cancel()
  # Wait until all worker tasks are cancelled.
  await asyncio.gather(*tasks, return_exceptions=True)

  print('====')
  print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
  print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

asyncio.run(main())

####################################################################################
# async def crawl(url):
#   # page= {}
#   async def get_page(url):
#     r = await asession.get(url)
#     return r
#   results = await get_page(url)
#   return results
#     # soup = bs(res.content, 'lxml')
#     # next_pgtxt = soup.find('div', class_='mw-allpages-nav').find('a').text.lower()
    # next_pghref = soup.find('div', class_='mw-allpages-nav').find('a').get('href')
    # if('next' in next_pgtxt):
    #   page['txt'] = next_pgtxt
    #   page['href'] = next_pghref
    #   pages.append(page)
    #   next_page = f'{BASE_URL}{next_pghref}'
  

# results = asession.run(crawl(f'{BASE_URL}{start_href}'))
# print(results.html.url)

# print(pages)


