# 10. Write a program to wipe out the content of a file using python.

with open('Hi-score.txt','w') as f:
    f.write('')
    print('The file content is wiped out successfully!')
