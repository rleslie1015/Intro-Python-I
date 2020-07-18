"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
printf_string = ("x is %s, y is %s, z is %s" % (x, y, z))
print(printf_string)

# Use the 'format' string method to print the same thing
txt = 'x is {:.2f}, y is {}, z is {:^8}'
formatted = txt.format(10, 2.24552, "I like turtles!")
print(formatted)

txt1 = "For only {price:.2f} dollars!"
print(txt1.format(price = 49))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is {z}')