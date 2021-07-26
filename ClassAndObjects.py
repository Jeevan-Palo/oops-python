# Class is a collection of Object or blueprint for the object
class Testing:
    # Instance Method: Eventhough we didn't pass any argument to method, we have to provide atleast one argument which
    # is self argument. self is a current object
    def manual(self):
        print("Manual Testing")


print(Testing)
# testObject is object of the class Testing
testObject = Testing()
testObject.manual()
# Verify object is belongs to the class Testing
print(isinstance(testObject, Testing))
