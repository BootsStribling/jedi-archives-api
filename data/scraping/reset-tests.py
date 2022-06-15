import os

def reset_starship_test():
  file_list = os.dirlist('../raw/starships')
  for file in file_list:
    os.rename(f'../raw/starships/{file}', f'../raw/a-z/{file}')

reset_starship_test()