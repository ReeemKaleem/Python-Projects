#import libraries 

import random 
from art import logo,stages 
from words import word_list 

#------ =display
# - - a - -
#user makes a guess ->  if the user guess correctly we fill in the blank
# if user makes an incorrect guess -- we decrease life
# continue till the game ends 
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives =6 
print(logo)

#creating blank spaces 
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    #user makes a guess 
    guess = input("guess a letter").lower()
    if guess in display:
        print("You have already guessed this letter ")
    for position in range(word_length):
        # chosen word = bcadb
        #guess by user is a 
        #initially display
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter 
    #check if user has made a wrong guess 
    if guess not in chosen_word:
        print("You guessed incorrectly.You have lost a life")
        lives = lives - 1
        if lives == 0:
            end_of_game = True 
            print("You lost the game... You have ) lives!")
            #join is used to convert a list into strings 
            #split strings to list 
            #list =[a,b,c]
            # a b c
            #'&'.join(list)
            #a&b&c
            #word.split("&")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True 
        print("hurray you've guessed correctly and won the game !")

    print(stages[lives])


#incorporate regular expression 
#easy and hard level 
#maybe we give hints to the user 
#give user different versions like words from animals books 
