# Write a program to print multiplication table of a given number using while loop

number = int(input("Enter the number : "))
start = 1

while start <= 10:
    print(f"{number} X {start} = {number * start}")
    start += 1
    