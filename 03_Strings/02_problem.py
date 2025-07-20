# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

result_template = ''' Dear <|Name|>,\n\tYou are selected!\n<|Date|>'''

print(result_template.replace('<|Name|>','Vishnu').replace('<|Date|>','15 July, 2025'))