from misc_modules import *
import sys
import os
from datetime import date, time, datetime, timedelta
import time as timetime
import calendar

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

sys.stderr.write("Dummy Error Test Message")

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

# OS
print("os.uname():", os.uname())
print("os.name:", os.name)
print("os.listdir():", os.listdir())
print("mkdir(\"./temp\"):", os.mkdir("./temp"))
print("os.getcwd():", os.getcwd())
print("os.chdir(\"./temp\"):", os.chdir("./temp"))
print("os.getcwd():", os.getcwd())
print("os.makedirs(\"1/2\"):", os.makedirs("1/2"))
print("os.listdir():", os.listdir())

print("os.removedirs(\"1/2\"):", os.removedirs("1/2"))
print("os.listdir():", os.listdir())
print("os.chdir(\"../\"):", os.chdir("../"))
print("os.listdir():", os.listdir())
print("os.rmdir(\"./temp\"):", os.rmdir("./temp"))
print("os.listdir():", os.listdir())
print("os.system(\"echo hello\"):", os.system("echo hello"))
print()

# Datetime
t = date.today()
print("date.today():", t)
print("day month year:", t.day, t.month, t.year)
print("new date first day of Epoch date(1970, 1, 1):", date(1970, 1, 1))
print("new date from iso format date.fromisoformat(\"1970-01-01\"):", date.fromisoformat("1970-01-01"))
print("date.fromtimestamp(86400):", date.fromtimestamp(86400))
print("d = date.fromisoformat(\"1970-01-01\")")
d = date.fromisoformat("1970-01-01")
print("d = d.replace(year=d.year+1)")
d = d.replace(year=d.year+1)
print("new date d:", d)
print("timetime.time()", timetime.time())
print("weekday: date.today().weekday()", date.today().weekday())
print("weekday: date.today().isoweekday()", date.today().isoweekday())
print("t = time(12,0,0,0)")
t = time(12, 0, 0, 0)
print("t:", t)
print("timetime.sleep(2)")
timetime.sleep(2)
print("woken up")
print("From Epoch to date timetime.ctime(timetime.time()):", timetime.ctime(timetime.time()))
print("UTC/GMT Time timetime.gmtime(timetime.time()):", timetime.gmtime(timetime.time()))
print("Localtime timetime.localtime(timetime.time()):", timetime.localtime(timetime.time()))
print("Struct to string timetime.asctime(timetime.localtime(timetime.time())):", timetime.asctime(timetime.localtime(timetime.time())))
print("Struct to Epoch timetime.mktime(timetime.localtime(timetime.time())):", timetime.mktime(timetime.localtime(timetime.time())))
print("timetime.strftime('%m-%d-%Y %H:%M'):", timetime.strftime('%m-%d-%Y %H:%M'))
print("timetime.strftime('%m-%d-%Y %H:%M',timetime.localtime(timetime.time())):", timetime.strftime('%m-%d-%Y %H:%M',timetime.localtime(timetime.time())))
print("datetime(1970,1,1):", datetime(1970, 1, 1))
print("datetime(1970,1,1).date():", datetime(1970, 1, 1).date())
print("datetime(1970,1,1).time():", datetime(1970, 1, 1).time())
print("datetime(1970,1,1).timestamp():", datetime(1970, 1, 1).timestamp())
print("datetime.strptime('2019/11/04 14:53:00', '%Y/%m/%d %H:%M:%S'):", datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
print("now MM-DD-YYYY datetime.now().strftime('%m-%d-%Y %H:%M'):", datetime.now().strftime('%m-%d-%Y %H:%M'))
print("now MM-DD-YYYY time(12,0).strftime('%H:%M %B'):", time(12, 0).strftime('%H:%M %B'))
print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
print("delta datetime.now()-datetime(1970,1,1):", datetime.now()-datetime(1970,1,1))
print("timedelta(weeks=2):", timedelta(weeks=2))
print("2 weeks*2 after Epoch time datetime(1970,1,1)+timedelta(weeks=2)*2:", datetime(1970, 1, 1)+timedelta(weeks=2)*2)
print("calendar.calendar(1970):", calendar.calendar(1970))
print("calendar.setfirstweekday(calendar.SUNDAY)")
calendar.setfirstweekday(calendar.SUNDAY)
print("calendar.month(1970, 1):", calendar.month(1970, 1))
print("calendar.weekday(1970, 1, 1):", calendar.weekday(1970, 1, 1))
print("calendar.weekheader(2)", calendar.weekheader(2))
print("calendar.isleap(1970):", calendar.isleap(1970))
print("calendar.leapdays(1970, 2000):", calendar.leapdays(1970, 2000))

a = datetime(2020,1,1,11,27,22)
b = datetime(2020,1,1,0,0,0)
print(a-b)
