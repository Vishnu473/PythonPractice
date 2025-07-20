# Write a program to find whether a given username contains less than 10
# characters or not. If less than 10, he is eligible to participate in contest1 , else contest2.

user_name = input("Enter your name: ")

if(len(user_name) < 10):
    print("You are eligible for contest 1")
else:
    print("You are eligible for contest 2")