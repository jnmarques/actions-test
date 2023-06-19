from importlib import import_module
#from scripts.print_time import print_time
import os
import time
import threading
import psutil
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, package_name, script_name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.script_name = script_name
      self.package_name = package_name

      self.module = import_module(self.package_name)
      self.code = getattr(self.module, self.script_name)
   def run(self):
      print("Starting " + self.name)
      self.code(self.name, 5, self.counter)
      print("Exiting " + self.name)


# Create new threads
thread1 = myThread(1, "Thread-1", 1,"scripts.print_time", "print_time")
thread2 = myThread(2, "Thread-2", 2,"scripts.print_time", "print_time")

# Start new Threads
thread1.start()
thread2.start()

while (True):
    current_process = psutil.Process(os.getpid())
    mem = current_process.memory_info().rss
    for child in current_process.children(recursive=True):
        print("Child: " + child.pid)
        mem += child.memory_info().rss

    print("HeartBeat mem: " + str(current_process.num_threads()) + ", " + str(mem))
    #print("Number Threads: " + )
    
    time.sleep(1)