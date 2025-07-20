# Write a program which finds out whether a given fruits liked by Ami is present in the fruits brought by you for Ami or not.

liked_fruits = ["Apple", "Banana", "Kiwi"]

fruits_brought = input("enter the fruit you brought for Ami: ")

if fruits_brought in liked_fruits:
    print(f"Thank you! I love this {fruits_brought}")
else:
    print(f"I don't like this {fruits_brought}")