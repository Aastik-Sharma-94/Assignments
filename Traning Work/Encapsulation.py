class A:
    __privateVariable = 2020
    def __privateMethod(self):
        print("I'm inside class A which is private method")
    def display(self):
        print("Private Variable: ",A.__privateVariable)
        self.__privateMethod()
ob = A()
ob.display()