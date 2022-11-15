# Import math
import math
# Import every entity
from math import *
# Module aliasing
import math as calc
# Entities aliasing
from math import sin as sen, pi as py

print("sin(pi/2): ", sin(pi/2))
print("calc.sin(calc.pi/2): ", calc.sin(calc.pi/2))
print("sen(py/2): ", sen(py/2))
print("degrees(py/2): ", degrees(py/2))
print("exp(1): ", exp(1))
print()

print("dir(math):")
for entity in dir(math):
    print(entity, end=" ")
print()

print("floor(1.3): ", floor(1.3))
print("ceil(1.3): ", ceil(1.3))
print("trunc(1.3): ", trunc(1.3))
print("hypot(3,4): ", hypot(3, 4))

