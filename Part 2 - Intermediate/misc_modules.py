import random


class IterClass:
    def __init__(self, n=10):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n > 0:
            return random.random()
        raise StopIteration


def generator(n=10):
    for i in range(n):
        yield random.random()


def powers_of_2(n):
    for i in range(n):
        yield 2**i


