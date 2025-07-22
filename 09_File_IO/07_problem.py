# 7. Write a program to find out the line number where python is present from ques 6.

with open('problem7.txt','r') as f:
    content = f.readlines()
print(len(content))
line_no=1
for line in content:
    if 'python' in line:
        print(f'Python is present in line number: {line_no}')
        break
    line_no += 1
else:
    print('Python is not present in the total file.')
