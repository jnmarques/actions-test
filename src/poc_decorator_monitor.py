from calendar import c
from math import e
import time
from decorators.monitored import monitored

@monitored(common_name="test_it_out")
def print_time(threadName, counter, delay, event):
    while counter:
        if(event.is_set()):
            print("Exiting gracefully")
            exit(0)
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

print_time("Thread-1", 100, 1)
    