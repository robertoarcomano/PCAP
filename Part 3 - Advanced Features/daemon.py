from threading import Thread
from time import sleep
from random import random


class MyDaemonThread(Thread):
    def run(self, alpha=False):
        print("Start daemon:", self.name)
        a = 2
        for i in range(100000000):
            a *= i / 1223
        print("\nEnd daemon:", self.name, "Ident:", self.ident, "Native ID:", self.native_id, a)


n = MyDaemonThread(name="n", daemon=True)
n.start()
print("n daemon:", n.daemon)
n.join()
