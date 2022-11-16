multiline = """
    hello
    everyone
"""
print("multiline:", multiline, "len(multiline):", len(multiline))
print("\"a\" + \"b\":", "a" + "b")
print("10 * \"a\":", 10 * "a")
print("ord(\"a\"):", ord("a"))
print("chr(ord(\"a\")):", chr(ord("a")))

s = "string"
sep = "#"
list_n = [4, 5, 1, 15, 51]
list_s = ["4", "5", "1", "15", "51"]
list_n1 = list_n[:]
list_s1 = list_s[:]
print("s:", s)
print("sep:", sep)
print("list_n:", list_n)
print("list_s:", list_s)
print("iteration:", end=" ")
for c in s:
    print(c, end=" ")
print()
print("indexing:", end=" ")
for i in range(len(s)):
    print(s[i], end=" ")
print()
print("slicing:", end=" ")
print("s[1:3]:", s[1:3], end=", ")
print("s[-3:-1]:", s[-3:-1])
print("in:", end=" ")
print("\"r\" in s:", "r" in s, end=", ")
print("\"i\" not in s:", "i" not in s)
print("Strings are immutable")
print("min(s):", min(s))
print("max(s):", max(s))
print("s.index(\"i\"):", s.index("i"))
print("list(s):", list(s))
print("s.count(\"i\"):", s.count("i"))
print("s.capitalize():", s.capitalize())
print("s.center(20,\"*\"):", s.center(20,"*"))
print("s.endswith(\"ng\"):", s.endswith("ng"))
print("s.startswith(\"str\"):", s.startswith("str"))
print("s.find(\"t\", 2, 4):", s.find("t", 2, 4))
print("s.isalnum():", s.isalnum())
print("s.isalpha():", s.isalpha())
print("s.isdigit():", s.isdigit())
print("s.islower():", s.islower())
print("s.isspace():", s.isspace())
print("s.isupper():", s.isupper())
print("sep.join([s, s]):", sep.join([s, s]))
print("s.lower():", s.lower())
print("s.upper():", s.upper())
print("(\" \" + s).lstrip():", (" " + s).lstrip())
print("(s + \" \").rstrip():", (s + " ").rstrip())
print("(\" \" + s + \" \").strip():", (" " + s + " ").strip())
print("s.replace(\"i\",\"e\", 1):", s.replace("i", "e", 1))
print("s.rfind(\"t\", 1, 4):", s.rfind("t", 1, 4))
print("sep.join([s, s]).split(sep):", sep.join([s, s]).split(sep))
print("s.capitalize().swapcase():", s.capitalize().swapcase())
print("(s + " " + s).title():", (s + " " + s).title())
print("s < s.capitalize():", s < s.capitalize())
print("list_n.sorted():", sorted(list_n))
print("list_s.sorted():", sorted(list_s))
list_n1.sort()
print("list_n1.sort()")
list_s1.sort()
print("list_s1.sort()")
print("list_n1:", list_n1)
print("list_s1:", list_s1)




