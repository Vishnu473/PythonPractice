# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d:
    print("b is greatest")
elif c>d:
    print("c is greatest")
else:
    print("d is greatest")