# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poems.txt",'r')
text = f.read()
if 'twinkle' in text:
    print('Twinkle is present in the file')
else:
    print('Twinkle is not present in the file')

f.close()