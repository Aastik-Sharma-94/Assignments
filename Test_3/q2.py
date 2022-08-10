# 2. Create an abstract class representing equilateral polygon with required abstract and concrete methods and properties to calculate area and perimeter of it. Create classes for Rectangle, Square and Regular Pentagon by implementing a polygon class to calculate the area and perimeter of them. 
# Also overload the comparison operators for above classes to compare them by their calculated area. 
# In the main function, ask the user number of sides and length of the polygon and print their area and perimeter accordingly

import math
from abc import ABC, abstractmethod
class polygon(ABC):
    def common(self):
        print("This is a concrete method")
    @abstractmethod # decorator
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Square(polygon):
    def __init__(self,side):
        self.__side=side        
    def area(self):
        return self.__side*self.__side    
    def perimeter(self):
        return 4*self.__side       

class Rectangle(polygon):
    def __init__(self,length,breath):
        self.__length=length
        self.__breath=breath        
    def area(self):
        return self.__length*self.__breath    
    def perimeter(self):
        return 2*(self.__length+self.__breath)
class pentagon(polygon):
    def __init__(self,border_length,radius):
        self.border_length=border_length
        self.radius=radius
    def area(self):
        return (5 * (int (self.border_length) * int (self.radius) )) / 2    
    def perimeter(self):
        return 5 * int(self.border_length)  
S1=Square(int(input("Enter the side of square::")))
print(S1.common())
print(S1.area())
print(S1.perimeter())
R1=Rectangle(int(input("Enter the length of rectangle ::")),int(input("Enter the breadth of rectangle ::")))
print(R1.common())
print(R1.area())
print(R1.perimeter())
P1=pentagon(int(input("Enter the border length ::")),int(input("Enter the radius ::")))
print(P1.common())
print(P1.area())
print(P1.perimeter())