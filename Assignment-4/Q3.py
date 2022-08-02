def status(age):
    if age<0:
        raise ValueError("only positive integers are allowed")
    if age>22:
        print("eligible for marrige")
    else:
        print("not eligible for marrige try after some time")
try:
    num =int(input("Enter your age:"))
    status(num)
except ValueError:
    print("Only positive integers are allowed you ......")
finally:
 	print("finally block....")