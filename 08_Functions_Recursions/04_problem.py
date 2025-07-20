# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter the number till which you wanna calculate the sum: "))


def sum_n(number):
    if(number == 1):
        return 1
    else:
        return number+sum_n(number-1)
    
sum_all_n = sum_n(n)
print(f"The sum of first {n} numbers is {sum_all_n}")