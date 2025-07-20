# Write a program to print multiplication table of a given number using for loop.

number = int(input("enter the number for which you wanna learn Table: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number *i}")