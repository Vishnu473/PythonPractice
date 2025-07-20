# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
mark1 = input("Enter the mark1: ")
marks.append(mark1)
mark2 = input("Enter the mark2: ")
marks.append(mark2)
mark3 = input("Enter the mark3: ")
marks.append(mark3)
mark4 = input("Enter the mark4: ")
marks.append(mark4)
mark5 = input("Enter the mark5: ")
marks.append(mark5)
mark6 = input("Enter the mark6: ")
marks.append(mark6)
mark7 = input("Enter the mark7: ")
marks.append(mark7)

print(f"You entered marks: {marks}")
marks.sort()
print(f"Your marks after sorting: {marks}")
