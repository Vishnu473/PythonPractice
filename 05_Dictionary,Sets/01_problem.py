# 1. Write a program to create a dictionary of Telugu words with values as their English translation. Provide user with an option to look it up!

words = {
    "namaskaram" : "Hello!",
    "Dhanyavadalu" : "Thanks",
    "Ela Unnaru" : "How are you?",
    "Emayyindhi" : "What happened?",
    "Hammayya" : "Thank God!",
}
print("The words you can learn are: ",words.keys())
userQuery = input("Enter the word you wanna know meaning : ")

print(f"The meaning of '{userQuery}' is '{words[userQuery]}'")