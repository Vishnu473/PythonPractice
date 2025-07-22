# 2. The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

from random import randint

def game():
    score = randint(2,200)
    
    print(f"The current score is {score}")
    with open("Hi-score.txt") as f:
        hi_score = f.read()
        if(hi_score == ''):
            hi_score = 0
        else:
            hi_score = int(hi_score)
        print(f"The previous hi-score is {hi_score}")
    

    if score > hi_score:
        with open("Hi-score.txt",'w') as f:
            f.write(f"{score}")
game()