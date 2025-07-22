# 5. Repeat program 4 for a list of such words to be censored.
toBe_censored_words = ["donkey","ugly","lazy"]

with open('problem5.txt','r') as f:
    content = f.read()

updated_content = content
for i in toBe_censored_words:
    print(i)
    updated_content = updated_content.replace(i,"#####")

with open('problem5.txt','w') as f:
    f.write(updated_content)