from itertools import count
from time import sleep

counter = 0
while True:
    counter += 1
    print("HELLO WORLD: " + str(counter))
    sleep(1)