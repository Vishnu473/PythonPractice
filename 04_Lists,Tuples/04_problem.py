# 4. Write a program to sum a list with 4 numbers.

num1 = int(input("enter the number1: "))
num2 = int(input("enter the number2: "))
num3 = int(input("enter the number3: "))
num4 = int(input("enter the number4: "))

lst = []
lst.append(num1)
lst.append(num2)
lst.append(num3)
lst.append(num4)

total = num1+num2+num3+num4
total1 = sum(lst)

print("The total sum is ", total)
print("The sum of numbers using list ",total1)