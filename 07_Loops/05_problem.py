# Write a program to find the sum of first n natural numbers using while loop

number = int(input("Enter the number till which you wanna sum: "))
start = 1
sum = 0
while (start <= number):
    sum += start
    start +=1 
print(f"Total sum of first {number}'s is {sum}")