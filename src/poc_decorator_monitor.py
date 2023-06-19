from calendar import c
import time
from decorators.monitored import monitored

@monitored(common_name="test_it_out")
def print_time(threadName, counter, delay):
   while counter:
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

print_time("Thread-1", 5, 1)
    