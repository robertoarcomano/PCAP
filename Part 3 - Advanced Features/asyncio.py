import asyncio
from time import sleep
from random import random


async def fn(alpha=False):
    start_ch = "1" if not alpha else "A"
    for i in range(9):
        string = chr(ord(start_ch) + i)
        print(string, end=" ")
        sleep(random()/10)

