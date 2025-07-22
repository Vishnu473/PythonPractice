# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open('problem6.txt','r') as f:
    content = f.read()

if 'Python' in content:
    print('Python word is present in the file')
else:
    print('Python word is not present in the file')
