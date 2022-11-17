from misc_modules import *
import sys

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
print()

print("filter(lambda x: x > 10, powers_of_2(10)): ", end=" ")
for i in filter(lambda x: x > 10, powers_of_2(10)):
    print(i, end=" ")
print()

power2 = power(2)
power10 = power(10)
print("power2(3):", power2(3))
print("power10(3):", power10(3))
print()

# File
header("/etc/hosts read char after char using the read(1)")
file = open("/etc/hosts", "rt")
ch = file.read(1)
count = 0
while ch != "":
    print(ch, end="")
    ch = file.read(1)
    count += 1
file.close()
print("total chars read: ", count)
print()

# File
header("/etc/hosts read line after line using readline()")
file = open("/etc/hosts", "rt")
line = file.readline()
count = 0
while line != "":
    print(count, line, end="")
    line = file.readline()
    count += 1
file.close()
print()

count = 0
header("/etc/hosts read at once using readlines()")
file = open("/etc/hosts", "rt")
lines = file.readlines()
file.close()
for line in lines:
    print(count, line, end="")
    count += 1
print()

header("/etc/hosts read at once using read()")
file = open("/etc/hosts", "rt")
text = file.read()
file.close()
print(text)
print()

header("/etc/hosts read iterating on open()")
for line in open("/etc/hosts", "rt"):
    print(line, end="")
print()

header("read /etc/hosts and write it to a new file indexing the lines")
file = open("./file", "wt")
lines = []
count = 0
for line in open("/etc/hosts", "rt"):
    file.write(str(count) + " " + line)
    count += 1
file.close()
print()

sys.stderr.write("Dummy Error message")

header("write binary data file")
data = bytearray(10)
for i in range(len(data)):
    data[i] = ord('a') + i
file = open("./filebin", "wb")
file.write(data)
file.close()
print()

header("read binary data file")
data = bytearray(10)
for i in range(len(data)):
    data[i] = ord('a') + i
file = open("./filebin", "rb")
file.readinto(data)
file.close()
print("data read from binary file: ", data)
print()

header("read binary data easier file")
file = open("./filebin", "rb")
data = bytearray(file.read())
file.close()
print("data read from binary file easier: ", end="")
for b in data:
    print(chr(b), end=" ")
print()
print()
