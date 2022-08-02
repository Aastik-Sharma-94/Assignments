class Person(object):
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name(self):
        return self.firstname+" " + self.lastname
class Employee(Person):
    def __init__(self, first, last, staffnum):
        super().__init__(first,last)
        #Person.__init__(self,first, last)
        self.staffnumber = staffnum
    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber
x = Person("Lachu", "Sharma")
y = Employee("Lachu", "Sharma", "19512")
print(x.Name())
print(y.GetEmployee())