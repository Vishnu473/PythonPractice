# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

spam_content = ["Make a lot of money", "buy now", "subscribe this", "click this"]

comment = input("Enter the comment: ")

for spam_text in spam_content:
    if spam_text.lower() in comment.lower():
        print("This comment is a spam.")
        break
else:
    print("The comment is not a spam")