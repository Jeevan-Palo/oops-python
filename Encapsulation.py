class Testing:
    def __init__(self, testTypes, experience):
        self.testTypess = testTypes
        self.__experience = experience

    def display(self):
        print(self.testTypess)
        # Private variable or method should be use (__) prefix the name of the variable and function
        # we can use sing underscore(_) but it is just for name convention.
        print(self.__experience)
        # Private method can access with in a class by using self object
        self.__private_method()

    def getAge(self):
        print(self.__experience)

    def setAge(self, experience):
        self.__experience = experience

    def __private_method(self):
        print("Private Method")


test_obj = Testing('Manual Testing', 5)
# call class method
test_obj.display()
# Changing experience value using setter method
test_obj.getAge()
test_obj.setAge(6)
test_obj.getAge()
print(test_obj.testTypess)
# Private variable and Method cannot access outside the class
# print(test_obj.__experience)
# test_obj.__private_method()
