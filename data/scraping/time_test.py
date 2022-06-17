import time

def time_test():
  before = time.monotonic()
  r = Timer(5.0, print_timer('timer ran'))
  r.start()
  after = time.monotonic()
  print(before)
  print(after)
  print(after - before)


time_test()