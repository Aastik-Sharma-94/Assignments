# Print the sum, difference and product of two complex numbers by creating a class named 'Complex' with separate methods
#  for each operation whose real and imaginary parts are entered by the user. 

class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))            

    def display(self):
        print(f"{self.realPart}+{self.imgPart}i")

    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart

    def diff(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart

    def mul(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart

c1 = Complex()
c2 = Complex()
c3 = Complex()

print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("-----------------------------------")

print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("-----------------------------------")

print("\nSum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()

print("\nDifference of two complex numbers is ", end="")
c3.diff(c1,c2)
c3.display()

print("\nProduct of two complex numbers is ", end="")
c3.mul(c1,c2)
c3.display()