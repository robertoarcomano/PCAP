class Void:
    pass


class Base(Void):
    def __init__(self, name=""):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Derived(Base):
    def __init__(self, name=""):
        self.__number_methods_called = 0
        Base.__init__(self, name)

    def get_number_methods_called(self):
        return self.__number_methods_called

    def get_name(self):
        self.__number_methods_called += 1
        return Base.get_name(self)

    def set_name(self, name):
        self.__number_methods_called += 1
        return Base.set_name(self, name)


object1 = Base("object1")
try:
    print(object1.__name)
except AttributeError:
    print("private attribute (starting with '__') are not accessible from outside the class")

print("object1.get_name():", object1.get_name())

object2 = Derived("object2")
print("object2.get_number_methods_called():", object2.get_number_methods_called())
print("object2.set_name")
object2.set_name("new name object2")
print("object2.get_number_methods_called():", object2.get_number_methods_called())
