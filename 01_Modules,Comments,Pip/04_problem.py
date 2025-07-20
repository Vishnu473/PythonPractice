# 4.Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# The directory you want to print the contents
current_directory = '/'

# Using try except block for printing the content files.
try:
    contents = os.listdir(current_directory)
    print(f"Contents of '{current_directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You don't have permission to access this directory.")