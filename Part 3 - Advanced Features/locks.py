from threading import Thread, Lock
from time import sleep
from random import random

lock = Lock()


def fn(name):
    for i in range(10):
        lock.acquire()
        print(name, "entered")
        sleep(random())
        print(name, "exiting")
        lock.release()
        sleep(random())


thread1 = Thread(target=fn, args=("t1",))
thread2 = Thread(target=fn, args=("t2",))

thread1.start()
thread2.start()


