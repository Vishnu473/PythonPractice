# Write a program to help Rajeev to buy the Mangos based on the quality from the machine he had:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

quality = int(input("Enter the quality of the fruit you got: "))

if(90 <= quality <= 100):
    print("This mango has 'Excellent' quality")
elif (80 <= quality < 90):
    print("This mango has 'A' quality")
elif (70 <= quality < 80):
    print("This mango has 'B' quality")
elif (60 <= quality < 70):
    print("This mango has 'C' quality")
elif (50 <= quality < 60):
    print("This mango has 'D' quality")
else:
    print("This mango has 'F' quality")