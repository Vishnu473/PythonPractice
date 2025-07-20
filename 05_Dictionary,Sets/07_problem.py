# 7. If the names of 2 friends are same; what will happen to the program in problem6?

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

# If the key is same, then th elast value is stored for the given key.

