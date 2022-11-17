from misc_modules import *

print("IterClass():", end=" ")
for i in IterClass():
    print(i, end=" ")
print()

print("generator():", end=" ")
for i in generator():
    print(i, end=" ")
print()

print("generator() using while and exception:", end=" ")
a = generator()
while True:
    try:
        next_value = a.__iter__().__next__()
        print(next_value, end=" ")
    except StopIteration:
        break
print()

print("powers_of_2(10):", end=" ")
for i in powers_of_2(10):
    print(i, end=" ")
print()
print("[x for x in powers_of_2(10)]:", [x for x in powers_of_2(10)])
print("(x for x in powers_of_2(10)):", (x for x in powers_of_2(10)))
print("list([x for x in powers_of_2(10)]):", list([x for x in powers_of_2(10)]))
print("5 in powers_of_2(10):", 5 in powers_of_2(10))
print("8 in powers_of_2(10):", 8 in powers_of_2(10))

print("map(lambda x: 1/x, powers_of_2(10)): ", end=" ")
for i in map(lambda x: 1/x, powers_of_2(10)):
    print(i, end=" ")
