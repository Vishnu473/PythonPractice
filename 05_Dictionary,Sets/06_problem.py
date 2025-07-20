# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dict = {}

user1 = input("Enter your name: ")
lang1 = input("Enter your favourite language: ")

user2 = input("Enter your friends name: ")
lang2 = input("enter your friend's favourite language: ")


user3 = input("Enter your friends name: ")
lang3 = input("enter your friend's favourite language: ")


user4 = input("Enter your friends name: ")
lang4 = input("enter your friend's favourite language: ")

dict.update({user1:lang1})
dict.update({user2:lang2})
dict.update({user3:lang3})
dict.update({user4:lang4})

print(dict)
