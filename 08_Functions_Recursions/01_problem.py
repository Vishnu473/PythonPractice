# Write a program using functions to find greatest of three numbers.

def greatest_of_all():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if(a>b and a>c):
        print(f"{a} is greatest of all")
    elif (b>c):
        print(f"{b} is greatest of all")
    else:
        print(f"{c} is greatest of all")

greatest_of_all()
