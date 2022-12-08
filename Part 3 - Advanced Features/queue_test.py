from collections import deque
from queue import Queue
from queue import LifoQueue

queue1 = deque()

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1.pop())
print(list1.pop())
print(list1.pop())
print()

queue1 = deque()
queue1.append(1)
queue1.append(2)
queue1.append(3)
print(queue1.pop())
print(queue1.pop())
print(queue1.pop())
print()

queue2 = Queue(maxsize=3)
queue2.put(1)
queue2.put(2)
print("queue2.full():", queue2.full())
queue2.put(3)
print("queue2.full():", queue2.full())
print(queue2.get())
print(queue2.get())
print(queue2.get())
print("queue2.empty():", queue2.empty())
print()

queue3 = LifoQueue(maxsize=3)
queue3.put(1)
queue3.put(2)
queue3.put(3)
print(queue3.get())
print(queue3.get())
print(queue3.get())
