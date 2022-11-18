class Void:
    count = 0

    @staticmethod
    def inc_count():
        Void.count += 1

    @staticmethod
    def get_count():
        return Void.count


class Base(Void):
    def __init__(self, name=""):
        self.__name = name

    def get_name(self):
        self.inc_count()
        return self.__name

    def set_name(self, name):
        self.inc_count()
        self.__name = name


class Derived(Base):
    def __init__(self, name=""):
        Base.__init__(self, name)

    def get_number_methods_called(self):
        pass
        # return self.__number_methods_called

    def get_name(self):
        return super().get_name()

    def set_name(self, name):
        # self.__number_methods_called += 1
        return Base.set_name(self, name)

    def __str__(self):
        return self.get_name()


# Accessibility
object1 = Base("object1")
try:
    print(object1.__name)
except AttributeError as e:
    print("private attribute (starting with '__') are not accessible from outside the class:", e)
    print("try this instead:")
    print("object1._Base__name:", object1._Base__name)
print()

# Simple methods calling
object2 = Derived("object2")
object2_cloned = object2
print("object2.get_count():", object2.get_count())
print("object2.set_name")
object2.set_name("new name object2")
print("object2.get_name():", object2.get_name())
print("object2.get_count():", object2.get_count())
print()

# Class Hierarchy
print("issubclass(Derived,Base):", issubclass(Derived, Base))
print("isinstance(object2,Derived):", isinstance(object2, Derived))
print("object2_cloned is object2:", object2_cloned is object2)
print()

# Use of __dict__
object1.test_variable = "ok"
print("object1.__dict__:", object1.__dict__)
print("object2.__dict__:", object2.__dict__)
print()

# Use of hasattr
print("hasattr(object1,\"__name\"):", hasattr(object1, "__name"))
print("hasattr(object1,\"test_variable\"):", hasattr(object1, "test_variable"))
print()

# Use of __str__
print("using __str__ object2:", object2)
print()

# Use of __bases__
print("Void.__bases__[0].__name__):", Void.__bases__[0].__name__)
print("Base.__bases__[0].__name__):", Base.__bases__[0].__name__)
print("Derived.__bases__[0].__name__):", Derived.__bases__[0].__name__)
print()

# getattr
print("getattr(object2, \"_Base__name\"):", getattr(object2, "_Base__name"))
print("setattr(object2, \"_Base__name\", \"another name for object2\")")
setattr(object2, "_Base__name", "another name for object2")
print("getattr(object2, \"_Base__name\"):", getattr(object2, "_Base__name"))

# TODO
# self.args on exceptions
# step of range as well as randint...

