# Inheritance - It is used for code reusability. A child class inherit the property and method from parent class
class Testing:
    def manual(self):
        print("Manual Tester")

# Child class Automation inherits property and method from the base class Testing


class Automation(Testing):
    def auto(self):
        print("Automation Tester")


automation = Automation()
automation.manual()
automation.auto()

print("===== Multi Level Inheritance =====")


class TestingParent:
    def manual(self):
        print("Manual Testing")

# Child class AutomationChild inherits property and method from the base class TestingParent


class AutomationChild(TestingParent):
    def auto(self):
        print("Automation Testing")

# Child class PerformanceChild inherits property and method from the base class TestingParent and AutomationChild


class PerformanceChild(AutomationChild):
    def perform(self):
        print("Performance Testing")


performanceChild = PerformanceChild()
performanceChild.perform()
performanceChild.auto()
performanceChild.manual()
automationChild = AutomationChild()
# automationChild.perform()


print("===== Multiple Inheritance =====")


class Base1:
    def base(self):
        print("Base class 1")


class Base2:
    def base2(self):
        print("Base class 2")

# There is no relationship between Base1 and Base2 but Child can inherits the property and method from  Base1 and Base2


class Child(Base1, Base2):
    def child(self):
        print("Child class")


child = Child()
child.base()
child.base2()
child.child()
# issubclass is used to check the relationship between the specified classes. It returns Boolean value
print(issubclass(Child, Base1))
print(issubclass(Base1, Base2))
# isinstance is used to check the relationship between object and class. It returns Boolean value
print(isinstance(child, Child))
print(isinstance(child, Base1))
