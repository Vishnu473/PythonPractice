# Write a python function which converts inches to cms.

inch = float(input("Enter the inches to convert to cm: "))

def inch_to_cm(n):
    return n*2.54

result_cm = inch_to_cm(inch)
print(f"{inch} inches is equivalent to {round(result_cm,2)} cms")

