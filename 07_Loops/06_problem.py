# Write a program to calculate the factorial of a given number using for loop.

number = int(input("enter the number you wanna find factorial: "))

result = 1
for i in range(1,number+1):
    result *= i

print(f"The factorial of {number} is {result}")