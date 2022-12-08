a="123"
match(a):
    case "1"|"2"|"12":
        print("1,2,12")
    case "4":
        print("4")
    case _:
        print("else")