"""Data types"""
a = 6
b = "python"
c = 4.89
d = 30 + 4j
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""Binary, Hexa, Octa Function"""
x = 15      
print(bin(x))        
print(hex(x))
print(oct(x))

"""String function"""
name = "Guneet"
print(name[4:9])
print(name[:9])
print(name[3:6])
print(name[4:])
print(name[:-1])
print(name[:-5])
print(name[-9:-4])
print(name[-7:])
print(name[-1:])

"""Slice function"""
a = ("a", "b", "c", "d","e", "f", "g", "h")
x = slice(2, 5)
print(a[x])

a = ("a", "b", "c", "d","e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

a = ("a", "b", "c", "d","e", "f", "g", "h")
x = slice(0, 5, 8)
print(a[x])

a = ("a", "b", "c", "d","e", "f", "g", "h")
x = slice(1,8)
print(a[x])

"""Sorted function"""
a = ("c", "f", "a", "d","h", "b", "g", "e")
x = sorted(a)
print(x)                                            #ascending

a = ("c", "f", "a", "d","h", "b", "g", "e")
x = sorted(a, reverse=True)
print(x)                                            #descending

"""string isupper()"""
a = "THIS IS PYTHON"
x = a.isupper()
print(x)

a = "python tutorial"
b = "class 12"
c = "PYTHON CLASS"
print(a.isupper())
print(b.isupper())
print(c.isupper())

"""string islower()"""
a = "this is python"
x = a.islower()
print(x)

a = "python tutorial"
b = "class 12"
c = "Python Class"
print(a.islower())
print(b.islower())
print(c.islower())

"""string upper()"""
a = "this is python"
x = a.upper()
print(x)

"""string lower()"""
a = "THIS IS PYTHON"
x = a.lower()
print(x)


"""Creating Variables"""
print("hello")
print(10*20)
print(50-5)
print("67+9")
print('6+8')

x = 8
y = "rahul"
print(x)
print(y)

x = 6                  # x is of type int
x = "Sam"              # x is now of type str
print(x)

"""Casting Variable"""
x = str(7)                  # x will be '7'
print(x)
y = int(7)                  # y will be 7
print(y)
z = float(7)                # z will be 7.0
print(z)

"""Get the type variable"""
x = 9876
y = "python"
print(type(x))
print(type(y))

"""Case-Sensitive Variable"""
x = 4567
X = "python class"
print(x)
print(X)

"""Variable names"""
myvar = "python"
my_var = "python"
_my_var = "python"
myVar = "python"
MYVAR = "python"
myvar2 = "python"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

"""Many Values to Multiple Variables"""
x, y, z = "orange", "white", "black"
print(x)
print(y)
print(z)

"""One Value to Multiple Variables"""
x = y = z = "python"
print(x)
print(y)
print(z)

"""Unpack a Collection"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""output variables"""
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

"""global variables"""
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

def new_func():
    x = "awesome"
    def myfunc():
      x = "fantastic"
      print("Python is " + x)
    myfunc()
    print("Python is " + x)

new_func()