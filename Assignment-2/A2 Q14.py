# Write a Python program to create a symmetric difference and set difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print(result)

# Output: {'a', 'b', 'e'}