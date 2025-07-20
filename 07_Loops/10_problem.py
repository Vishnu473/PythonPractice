# Write a program to print multiplication table of n using for loops in reversed order

n = int(input("enter the number table you want in reversed order: "))

for i in range(0,n):
    print(f"{n} X {n-i} = {n*(n-i)}")