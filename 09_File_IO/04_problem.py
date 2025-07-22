# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("problem4.txt",'r') as f:
    content = f.read()

updated_content = content.replace("donkey","#####")

with open("problem4.txt",'w') as f:
    f.write(updated_content)


