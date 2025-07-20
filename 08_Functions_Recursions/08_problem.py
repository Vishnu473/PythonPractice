# Write a python function to print multiplication table of a given number

def multiply(n,start=1):
    if(start == 11):
        return
    print(f"{n} X {start} = {n*start}")
    multiply(n,start+1)

n = int(input("Enter the number to print table: "))
multiply(n)