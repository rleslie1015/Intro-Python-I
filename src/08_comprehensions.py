"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
# long way 
# for x in range(5):
#     y.append(x+1)
y = [x+1 for x in range(5)]
print(y)

squares = [num*num for num in y]
print(squares)
# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubes = [num**3 for num in y]

print(cubes)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [s.upper() for s in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

# Since `x` is a string, the `%` operator is treated as a string
# interpolation operator. The error occurs because no format specifier
# is provided.

# This tells the compiler that % is used as the modulus operator
y = [num for num in x if int(num) % 2 == 0]

print(y) 

