# Python Program to Reverse List using While Loop
NumList = []

Number = int(input("Please enter the Total Numbers : "))
for i in range(1, Number + 1):
    value = int(input("%d Element : " % i))
    NumList.append(value)

j = Number - 1
i = 0

while (i < j):
    temp = NumList[i]
    NumList[i] = NumList[j]
    NumList[j] = temp
    i = i + 1
    j = j - 1

print("\nThe Result =  ", NumList)