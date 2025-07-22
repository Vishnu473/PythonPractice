# 11. Write a python program to rename a file to “renamed_by_ python.txt.

import os

def rename_file(old_name,new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed successfully to {new_name}")
    except FileNotFoundError:
        print(f"Error: The file '{old_name}' does not exist.")
    except PermissionError:
        print("Error: Permission denied while renaming the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

rename_file('poems.txt','renamed_by_python.txt')