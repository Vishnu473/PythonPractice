# 8. Write a program to make a copy of a text file “this. txt”

with open('problem7.txt','r') as f:
    content = f.read()

with open('problem8.txt','w') as f:
    f.write(content)