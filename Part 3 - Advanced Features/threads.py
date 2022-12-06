import threading
import time
import random


def fn(alpha=False):
    start_ch = "1" if not alpha else "A"
    for i in range(9):
        string = chr(ord(start_ch) + i)
        print(string, end=" ")
        time.sleep(random.random()/10)


x = threading.Thread(target=fn)
y = threading.Thread(target=fn, args={True})
x.start()
y.start()
