# Write a python program using function to convert Celsius to Fahrenheit.

n = float(input("Enter the temperature(in Celsius) to know Fahrenheit value: "))

def celsius_to_fah(temp):
    return (temp*(9/5)) + 32


fah_temp = celsius_to_fah(n)
print(f"The {n}(in celsius) is equivalent to {round(fah_temp,2)} Fahrenheit.")