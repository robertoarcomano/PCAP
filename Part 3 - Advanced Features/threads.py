from threading import Thread
from time import sleep
import random


def fn(alpha=False):
    start_ch = "1" if not alpha else "A"
    for i in range(9):
        string = chr(ord(start_ch) + i)
        print(string, end=" ")
        sleep(random.random()/10)


x = Thread(target=fn)
y = Thread(target=fn, args={True})
x.start()
y.start()
