# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def generate_table(table):
    table_str = ""
    for i in range(1,11):
         table_str += f"{table} X {i} = {table*i}\n"
    with open(f"files/{table}_table.txt","w") as f:
        f.write(table_str)



for i in range(2,21):
    generate_table(i)