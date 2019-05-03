import random
# import only system to know OS type and store in the variable "name"
from os import system, name 
# import sleep to show output for some time period 
from time import sleep

#the default dictionary which will run no matter what
global cwords
cwords=['rainbow', 'dart', 'general', 'chemical', 'humble', 'family', 
           'dramatic', 'gland', 'arm', 'identical', 'mushroom', 'whale', 
           'charm', 'comet', 'cultural', 'first', 'align', 'rich', 'India', 
           'hump', 'fluid', 'bite', 'fighter', 'photograph', 'escalator', 
           'rose', 'horse', 'jumble', 'happiness','destruction', 
           'science', 'computer', 'programming', 'player', 'cheater']


def additem():
    
    file= open("dictionaryofwords.txt","a+")
    ch='y'
    while (ch=='y' or ch=='Y'):
        word = input("Enter the word :")
        ch= input("Enter another word? y/n :") 
        file.write(' ')
        file.write(word)
    print("Thank You for adding those amazing words! Let us make this game more fun!!!")
    
    
def choose():
    try:
        file= open("dictionaryofwords.txt","r+")
        line = file.read()
        dictionary=[]
        for u in line.split():
            dictionary.append(u) 
        pick=random.choice(dictionary)
        return pick


                
    except:
        global cwords
        pick=random.choice(cwords)
        return pick


# This function is created to clear the screen
def wipeScreen():
    # Clear command for windows
    if name == 'nt':
        _ = system('cls')
    # Clear command for mac and linux
    else:
        _ = system('clear') 
    # To add some empty vertical space from the top
    print('\n'*5) 


# This function is responsible for jumbling
def jumble(rec_word):
    jumbled=rec_word
    while (jumbled == rec_word):
        jumbled="".join(random.sample(rec_word,len(rec_word)))
    return jumbled

# This function is responsible for the final score.
def thank(p1n, p2n, s1, s2):
    wipeScreen()
    print(p1n, "Your final score is: ", s1)
    print(p2n, "Your final score is: ", s2)
    if s1>s2:
        print(p1n, "You win! ")
    elif s1<s2:
        print(p2n, "You win! ")
    else:
        print(p1n," and ",p2n, " you both are a same level genius! Its a draw!! ")
    print("I hope you enjoyed playing. \nHave a nice day!")

# This function is responsible to check the user answer and chances.
def j_game(player, score, pword, jword):
    wipeScreen()
    sleep(0.5)
    print("\t"*3, player.capitalize(), "it's your turn!\n")
    #Below print is just for decoration
    print("*"*25)
    print("Guess this word: ", jword)
    for chance in range(1,4):
        print("Chance", chance)
        answer=str(input("- What is your guess: "))
        if answer==pword:
            score=score+1
            print("\nYou scored", score, "point(s)!")
            break
        else:
            print("Try again.")
    print("\nCorrect answer is: ", pword)
    #sleep for 1 second
    sleep(1)
    return score

def play():
    wipeScreen()
    sleep(0.5)
    name_p1=str(input("Player 1, Please enter your name: "))
    name_p2=str(input("Player 2, Please enter your name: "))
    player_rounds=str(input("How many rounds do you want to play? "))

    #modifications for addition of words to make the program prosper

    if player_rounds=='create':
        #creation algorithms applied
        rounds=0
        print("Enter the password")
        passwrd=input()
        if passwrd=="jumble123":
            additem()
        else :
            print("Incorrect Password!")
            exit(0)


        
    else:
        rounds=int(player_rounds)
    
    

    # Cheating part. (Not yet updated/Added). I dont know English much.
    # So, i want this cheat.
    
    # As this is a two player game, we need 2 while loop runs to finish one round.
    # So we are doubling the round count here.
    rounds = rounds*2
    turn=0
    score_p1=0
    score_p2=0

    # Main game loop starts here
    while (turn < rounds):
        #Program chooses a random word from the above list
        picked_word=choose()
        #Picked word is jumbled here
        jumbled_word=jumble(picked_word)
        
        #Player1
        if turn%2 == 0:
            #We have created a j_game function. it will manage the game part.
            score_p1=j_game(name_p1, score_p1, picked_word, jumbled_word)

        #Player2
        else:
            #We have created a j_game function. it will manage the game part.
            score_p2=j_game(name_p2, score_p2, picked_word, jumbled_word)
                
        #turn increment 
        turn=turn+1
        if turn < rounds:
            #Player choice to Quit
            cont=int(input("Do you want to continue? \n press 1 to continue or 0 to quit: "))
            if cont == 0:
                break
    
    #Exit greetings
    thank(name_p1, name_p2, score_p1, score_p2)
    # Main game loop ends here

# Entire game starts because of this below "play()" function call.
play()
