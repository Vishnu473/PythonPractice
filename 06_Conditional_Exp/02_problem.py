# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# ai = int(input("Enter marks in AI: "))
# ml = int(input("Enter marks in ML: "))
# genAi = int(input("Enter marks in GenAI: "))

# total = ((ai+ml+genAi)/300)*100

# if (ai >= 33 and ml >= 33 and genAi >= 33) and total >= 40:
#     print("Congo! You have successfully Passed")
# else:
#     print("You need some more practice. Try again! Good Luck!")


#------------ OR -------------#

# marks = []
# marks.append(ai)
# marks.append(ml)
# marks.append(genAi)

# total = (sum(marks)/(len(marks)*100))*100
# failed_individual_subject = False

# for mark in marks:
#     if mark < 33:
#         failed_individual_subject = True
#         break
# if not failed_individual_subject and total >= 40:
#     print("Congo! You had passed!")
# else:
#     print("You need to practice more! Good Luck!")


# ---------------- OR --------------#

def get_valid_marks(subject_name):

    while True:
        try:
            marks = int(input(f"Enter the marks of {subject_name}: "))
            if(0 <= marks <= 100):
                return marks
            else:
                print("Incorrect marks entered. Enter marks in range from 0 to 100")
        except:
            print("Error! Enter valid mark in range from o to 100")

marks = []
ai = get_valid_marks("AI")
ml = get_valid_marks("ML")
genAI = get_valid_marks("GenAI")

# From here continue 1st approach or second approach
# Going with second approach
marks.append(ai)
marks.append(ml)
marks.append(genAI)

total = (sum(marks)/(len(marks)*100))*100

failed_subject = False

for mark in marks:
    if mark < 33:
        failed_subject = True
        break

if not failed_subject and total >= 40:
    print("Congo Buddy! You had passed the test successfully")
else:
    print("Need more preperation. Good Luck!")



    