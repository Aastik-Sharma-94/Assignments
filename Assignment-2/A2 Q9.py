# Python Program to find Sum of all Elements in a List

NumList = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

total = sum(NumList)

print("\n The Sum of All Element in this List is : ", total)