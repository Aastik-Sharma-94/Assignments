def a_fun():
 global name
 name = 'A'
def b_fun():
 global name
 name = 'B'
b_fun()
a_fun()
print (name)
"""output:-
PS C:\Users\Dell\Documents\assignment-3> python -u "c:\Users\Dell\Documents\assignment-3\q1.py"
A
PS C:\Users\Dell\Documents\assignment-3> 
 """