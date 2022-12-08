s1 = {1, 2, 2, 3}
print("s1:", s1)
s2 = {2, 3, 4, 4}
print("s2:", s2)
s3 = {2, 3}
print("s3:", s3)
print("s1.union(s2):", s1.union(s2))
print("s1.intersection(s2):", s2.intersection(s2))
print("s3.issubset(s2):", s3.issubset(s2))
print("s1.issubset(s2):", s1.issubset(s2))
print("s2.issuperset(s3):", s2.issuperset(s3))
print("s2.difference(s3):", s2.difference(s3))
print("s2.symmetric_difference(s3):", s2.symmetric_difference(s3))
print("s3.difference(s2):", s3.difference(s2))
print("s3.symmetric_difference(s2):", s3.symmetric_difference(s2))

