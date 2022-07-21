"""	Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
a.	Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}"""
def dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('green', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(dictionary(colors))