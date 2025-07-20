# Write a program to find whether a given number is prime or not

# A number is said to be prime if only 1 and itself is divisible

n = int(input("Enter the number to check prime or not: "))

for i in range(2,n):
    if(n%i) == 0:
        print(f"{n} is not a Prime number")
        break
else:
    print(f"{n} is a prime")