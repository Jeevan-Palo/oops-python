# Abstraction is the process of hiding the real implementation of an application from the user
# ‘abc’ is the module to be imported to use abstract class, ABC - Abstract Base Class
from abc import ABC, abstractmethod


class Testing(ABC):
    def __init__(self, x):
        print("Test", x)

    @abstractmethod
    def absmethod(self): pass

    @abstractmethod
    def absmethod1(self): pass


class TestChild(Testing):
    def Auto(self):
        print("Automation Testing")

    def absmethod(self):
        print("Implementation of abstract method 1 in subclass")

# Comment the below method to see the error for Abstract method must be implemented in child class
    def absmethod1(self):
        print("Implementation of abstract method 2 in subclass")


# uncommand the line number 19 to test Can't instantiate abstract class Testing with abstract method
# testing = Testing()
testChild = TestChild(100)
testChild.Auto()
testChild.absmethod()
