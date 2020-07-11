# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even(num):
    if (num % 2 == 0):
        print("Even!")
    elif (num % 2 == 1):
        print("Odd")
    else:
        print("Please enter a number.")
        input("Enter a number: ")

is_even(num)