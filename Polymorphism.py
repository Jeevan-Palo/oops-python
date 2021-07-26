# Polymorphism achieved through Overloading and Overriding
# Overriding - Two methods with the same name but doing different tasks, one method overrides the other
# It is achieved via Inheritance
class Testing:

    def manual(self):
        print('Automation Tester with 5 years Experience')


class ManualTest(Testing):

    def manual(self):
        super().manual()
        print('Manual Tester with 5 years Experience')


test = ManualTest()
test.manual()

# Method Overloading

# Python does not support method overloading by default
# Method overloading in Python is that we may overload the methods but can only use the latest defined method.
# The below example object will call same method with and without parameter


class Testing_MOL:
    def Hello(self, testing=None):
        if testing is not None:
            print('Hello ' + testing)
        else:
            print('Hello Manual Tester')


# Create an instance
obj = Testing_MOL()

# Call the method
obj.Hello()

# Call the method with a parameter
obj.Hello('Automnation Tester')
