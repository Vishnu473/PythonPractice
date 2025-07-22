# 9. Write a program to find out whether a file is identical & matches the content of another file.

def file_matched(file1, file2):

    with open(f'{file1}','r') as f:
        file1_content = f.read()

    with open(f'{file2}','r') as f:
        file2_content = f.read()

    if(file1_content == file2_content):
        print('The both files are identical and matches the content.')
    else:
        print('The both files are not identical.')

file_matched('problem7.txt','problem8.txt')