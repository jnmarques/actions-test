import threading
import os
import psutil
from time import perf_counter, sleep

def monitored(common_name = None):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.start()
            
            current_process = psutil.Process(os.getpid())
            child_process = psutil.Process(thread.native_id)
            process_name = common_name if common_name else fn.__name__
            while (child_process.is_running()):
                mem = current_process.memory_info().rss + child_process.memory_info().rss
                print("[ "+ process_name +" ] HeartBeat: " + str(current_process.num_threads()) + ", " + str(mem))
                
                sleep(0.5)
        return wrapper

    return decorator