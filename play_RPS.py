from random import randint
from time import sleep

option=['R','P','S']
LOSS_MESSAGE="YOU Lost!"
WIN_MESSAGE="You win!"
def decide_winner(user_choice,computer_choice):
    print "YOU SELECTED: %s" %user_choice
    print "Computer selecting...."
    sleep(1)
    print "She choice: %s"%computer_choice
    sleep(1)
    user_choice_index=int(option.index(user_choice))
    computer_choice_index=int(option.index(computer_choice))
    
    if computer_choice_index==user_choice_index:
        print "it's a tie"
    elif user_choice_index - computer_choice_index==1:
        print WIN_MESSAGE
    elif computer_choice_index - user_choice_index==1:
        print LOSS_MESSAGE
    else:
        print "Don't cheat"
        return

def play_RPS():
    print "Make a choice!"
    choice=raw_input("do it R,P,S:")
    C=str(choice.upper())
    CC=option[randint(0,2)]
    if C not in option:
        print "cheat"
        return
    decide_winner(C,CC)

play_RPS()

        
