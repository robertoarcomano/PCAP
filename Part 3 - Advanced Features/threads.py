from threading import Thread
from time import sleep
from random import random


class MyThread(Thread):
    def run(self, alpha=False):
        print("Beginning:", self.name)
        start_ch = "1" if not alpha else "A"
        for i in range(9):
            string = chr(ord(start_ch) + i)
            print(string, end=" ")
            sleep(random()/10)
        print("\nEnding:", self.name, "Ident:", self.ident, "Native ID:", self.native_id)


n = MyThread(name="n")
a = MyThread(kwargs={"alpha": True}, name="a")
n.start()
a.start()

print("\nn is alive:", n.is_alive())
print("\na is alive:", a.is_alive())

n.join()
a.join()
print("Threads joined")

print("n is alive:", n.is_alive())
print("a is alive:", a.is_alive())
