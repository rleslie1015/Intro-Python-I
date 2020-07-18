"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
s1 = slice(1,2)
print(a[s1])

# Output the second-to-last element: 9
s2 = slice(4,5)
print(a[s2])

# Output the last three elements in the array: [7, 9, 6]
s3 = slice(3,6)
print(a[s3])

# Output the two middle elements in the array: [1, 7]
s4 = slice(2,4)
print(a[s4])

# Output every element except the first one: [4, 1, 7, 9, 6]
s5 = slice(1, 6)
print(a[s5])

# Output every element except the last one: [2, 4, 1, 7, 9]
s5 = slice(0,5)
print(a[s5])

# For string s...

s = "Hello, world!"
s6 = slice(7, 12)
# Output just the 8th-12th characters: "world"
print(s[s6])