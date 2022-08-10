from abc import ABC,abstractmethod
 
class Animal(ABC):
 
    def sleep(self):
        print("I am going to sleep in a while")
 
    @abstractmethod
    def sound(self):
      pass

 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")
c = Cat()
c.sleep()
c.sound()