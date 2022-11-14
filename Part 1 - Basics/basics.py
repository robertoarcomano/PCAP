# hex, binary, conversions
age_s = "47"
age_d = int(age_s)
age_h = 0x2F
age_b = 0b101111
print("age_h: " + str(age_h) + " age_b: " + str(age_b))
print("age_d * 2: " + str(age_d * 2))
a = "1"
b = "2"
print("a: " + a + " b: " + b)
print("a, b = b, a")
a, b = b, a
print("a: " + a + " b: " + b)

# else loop
i = 22
for i in range(1, 3):
    print(i, end=" ")
else:
    print(i)

# logic
a = 22
b = 0
c = 0
print("(a or b) and (not c): " + str((a or b) and (not c)))

# bitwise logic
mask = 0b110000
print("mask: " + str(mask) + " age_b & mask: " + str(age_b & mask))
print("mask: " + str(mask) + " age_b | mask: " + str(age_b | mask))
print("mask: " + str(mask) + " ~mask: " + str(~mask))
print("mask: " + str(mask) + " mask << 3: " + str(mask << 3))
print("mask: " + str(mask) + " age_b ^ mask: " + str(age_b ^ mask))

# lists
names = ["Roberto", "Antonio", "John"]
print("names: " + str(names) + " len(names): " + str(len(names)))
print("names[0]: " + names[0])
print("names[-1]: " + names[-1])
print("del names[0]")
del names[0]
print("names: " + str(names) + " len(names): " + str(len(names)))
print("names.append(\"Frank`\"")
names.append("Frank")
print("names: " + str(names) + " len(names): " + str(len(names)))
print("names.insert(0,\"Roberto`\")")
names.insert(0, "Roberto")
print("names: " + str(names) + " len(names): " + str(len(names)))
print("names[0], names[2] = names[2], names[0]")
names[0], names[2] = names[2], names[0]
print("names: " + str(names) + " len(names): " + str(len(names)))
print("names.sort()")
names.sort()
print("names: " + str(names))
print("names1 = names")
names1 = names
print("names2 = names[:]")
names2 = names[:]
print("names.reverse()")
names.reverse()
print("names: " + str(names))
print("names1: " + str(names1))
print("names2: " + str(names2))
print("names2[0:2]: " + str(names2[0:2]))
print("names2[-2:-1]: " + str(names2[-3:-1]))
print("names2[-2:2]: " + str(names2[-2:-2]))
print("names2[:1]: " + str(names2[:1]))
print("names2[1:]: " + str(names2[1:]))
print("\"Frank\" in names2: " + str("Frank" in names2))
print("del names2[:2]")
del names2[:2]
print("names2: " + str(names2))
print("\"Frank\" in names2: " + str("Frank" in names2))
print("\"Frank\" not in names2: " + str("Frank" not in names2))
try:
    del names2
    print("names2: " + str(names2))
except:
    print()

print("[x**2 for x in range(5) if x % 2 == 0]: " + str([x**2 for x in range(5) if x % 2 == 0]))
print("[[x**2 for x in range(5) if x % 2 == 0] for j in range(3)]: " + str([[x**2 for x in range(5) if x % 2 == 0] for j in range(3)]))
