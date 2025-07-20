# Write a python function to remove a given word from a list ad strip it at the same time

list = ["Kiwi", "Krishna", "Ravan", "Lakshman", "Apple", "Bamboo", "an", "Raman"]

# strip() looks at the end of "Krishna". It finds 'a' (which is in "an"). It removes 'a'. The string becomes "Krishn".
# strip() then looks at the end of "Krishn". It finds 'n' (which is in "an"). It removes 'n'. The string becomes "Krish".
# strip() then looks at the end of "Krish". It finds 'h'. 'h' is not in "an". So, it stops removing characters from the end.
# strip() also checks the beginning, but 'K' is not in "an", so nothing is removed from the start.
# Therefore, "Krishna" becomes "Krish".

word = input("Enter the word to remove and strip at the same time: ")

def remo_strip(list,word):
    result = []
    for wrd in list:
        if not(wrd == word):
            result.append(wrd.strip(word))

    return result

result = remo_strip(list,word)
print(f"The resultant list after removing {word} from above list is {result}")