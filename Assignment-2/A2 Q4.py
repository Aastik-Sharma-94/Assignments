# star pattern

n = int(input("Enter the number of rows"))
for i in range(0, n):

    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

        # ending line after each row
    print(" ")