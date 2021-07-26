# Constructor used to create an object. Constructor implementation is little bit different from other language
class TestConstructor:
    # __init__() simulate the constructor of a class. This method is called when the class is instantiated.
    # Self is a first argument which allows accessing the attributes or method of the class.
    def __init__(self, testingTypes, experience):
        self.types = testingTypes
        self.years = experience

    def display(self):
        print(self.types, self.years)


obj_TestConstructor = TestConstructor("Manual Testing", 5)
onj1_TestConstructor = TestConstructor("Automation Testing", 6)

obj_TestConstructor.display()
onj1_TestConstructor.display()

# Types of Constructor

# 1. Non-Parametrized constructor


class Nonparam:
    def __init__(self):
        print("Non Parametrized")

    def show(self, testtype):
        print("Testtype = ", testtype)


nonparam = Nonparam()
nonparam.show("Performance Test")

# 2. Parametrized constructor


class Param:
    def __init__(self, testtype):
        print("Parametrized")
        self.testtype = testtype

    def show(self):
        print("Testtype = ", self.testtype)


param = Param("Manual Tester")
param.show()
