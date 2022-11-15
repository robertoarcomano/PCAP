# Import math
import math
# Import every entity
from math import *
# Module aliasing
import math as calc
# Entities aliasing
from math import sin as sen, pi as py
# Random
from random import random, seed, randrange, randint, choice, sample
# Platform
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
# Sys
import sys
sys.path.append("modules")
import my_module

# Dir
print("dir(math):")
for entity in dir(math):
    print(entity, end=" ")
print()

# Math
print("sin(pi/2): ", sin(pi/2))
print("calc.sin(calc.pi/2): ", calc.sin(calc.pi/2))
print("sen(py/2): ", sen(py/2))
print("degrees(py/2): ", degrees(py/2))
print("exp(1): ", exp(1))
print("floor(1.3): ", floor(1.3))
print("ceil(1.3): ", ceil(1.3))
print("trunc(1.3): ", trunc(1.3))
print("pow(2,3): ", pow(2, 3))
print("hypot(3,4): ", hypot(3, 4))
print()

# Random
print("seed(0): ", seed(0))
print("random(): ", random())
print("randrange(1,100,3): ", randrange(1, 100, 3))
print("randint(0,1): ", randint(0, 1))
list1 = [x for x in range(10)]
print("choice(list1): ", choice(list1))
print("sample(list1, 3): ", sample(list1, 3))
print()

# HW
print("platform(): ", platform())
print("machine(): ", machine())
print("processor(): ", processor())
print("system(): ", system())
print("version(): ", version())
print("python_implementation(): ", python_implementation())
print("python_version_tuple(): ", python_version_tuple())
print()

# Module
print("my_module.__counter:", my_module.__counter)
list1 = [1, 2, 3]
my_module.show_list(list1)
print("my_module.__counter:", my_module.__counter)
my_module.show_list(list1)
print("my_module.__counter:", my_module.__counter)

