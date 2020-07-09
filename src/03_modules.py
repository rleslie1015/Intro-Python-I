"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

#notes 
# what is a script? answer: a program

import sys

import fileinput
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# args = sys.argv
# print("sys.argv is: ")
# print(args)
print("file input is: ")
# for line in fileinput.input():
#     print(line)

# Print out the OS platform you're using:
# YOUR CODE HERE
print('os platform is: ')
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print('Python version is ')
print(sys.version_info)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
proccess_id = os.getpid()
print("current process id")
print(proccess_id)
# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print("current wokring dir is ")
print(cwd)

# Print out your machine's login name
# YOUR CODE HERE
login = os.getlogin()
print('machine\'s login name is ')
print(login)