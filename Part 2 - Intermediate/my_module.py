__counter = 0

if __name__ == "__main__":
    print("direct execution of the module")
else:
    print("module", __name__, "imported")


def show_list(list_in):
    global __counter
    __counter += 1
    print("list: ", end="")
    for item in list_in:
        print(item, end=" ")
    print()


