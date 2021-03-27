


from random import randint
from gamecomponents import gameVars,winLose




while gameVars.player_choice is False:
    print("=====###########=====*/ RPS GAME */=====###########=====")
    print("=====###########=====*/ RPS GAME */=====###########=====")

    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

    print("Choose your weapon! Or type quit to exit\n")

    gameVars.player_choice = input("choose rock, paper, or scissors: \n ")

    if gameVars.player_choice == "quit":
        print("===========OK GOODBYE !!! COMEBACK SOON===========")
        exit()

        
    print("user chose: " + gameVars.player_choice)

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice: 
        print("tie")
        
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print("OHH NO!!  you lose!")
            gameVars.player_lives -= 1
        else:
            print("OHH YEAH!!  you win!")
            gameVars.computer_lives -= 1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print("OHH YEAH!! you win!")
            gameVars.computer_lives -= 1

        else:
            print("OHH NO!!you lose!")
            gameVars.player_lives -= 1
            
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            print("OHH NO!!ROCKyou lose!")
            gameVars.player_lives -= 1
        else: 
            print("OHH YEAH!! you win!")  
            gameVars.computer_lives -= 1
    
   
    if gameVars.player_lives == 0:
        winLose.winorlose("lose..........GET OUT LOOSER")
    
    if gameVars.computer_lives == 0:
        winLose.winorlose("won.......THE KING IS BACK")
        
    
    print("player lives:", gameVars.player_lives)
    print("computer lives:", gameVars.computer_lives)


    gameVars.player_choice = False
=======
choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3


#player_choice = choices[1] 

player_choice = False



def winorlose(status):
    #print("inside winorlose function; status is: ",status)
    print("You", status, "! Would you like to play again?")
    choice = input("Y / N? ")

    if choice == "N" or choice == "n":
        print("you chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":


        global player_lives
        global computer_lives
        global total_lives

        player_lives = total_lives
        computer_lives = total_lives
    else:
        print("Make a valid choice - Y or N")
        choice = input("Y / N?")

while player_choice is False:
    print("=======================*/ RPS GAME */=======================")
    print("Computer Lives:", computer_lives, "/", total_lives)
    print("Player Lives:", player_lives, "/", total_lives)
    print("============================================================")

    print("Choose your weapon! Or type quit to exit\n")

    player_choice = input("choose rock, paper, or scissors: \n ")

    if player_choice == "quit":
        print("You chose to quit")
        exit()

        
    print("user chose: " + player_choice)

    computer_choice = choices[randint(0, 2)]
    print("computer chose: " + computer_choice)

    if computer_choice == player_choice: 
        print("tie")
        
    elif computer_choice == "rock":
        if player_choice == "scissors":
            print("you lose!")
            player_lives -= 1
        else:
            print("you win!")
            computer_lives -= 1

    elif computer_choice == "paper":
        if player_choice == "scissors":
            print("you win!")
            computer_lives -= 1

        else:
            print("you lose!")
            player_lives -= 1
            
    elif computer_choice == "scissors":
        if player_choice == "paper":
            print("you lose!")
            player_lives -= 1
        else: 
            print("you win!")  
            computer_lives -= 1
    
   
    if player_lives == 0:
        winorlose("lose")
    
    if computer_lives == 0:
        winorlose("won")
        
    
    print("player lives:", player_lives)
    print("computer lives:", computer_lives)


    player_choice = False
=======
if computer_choice == player_choice: 
    print("tie")
    
elif computer_choice == "rock":
    if player_choice == "scissors":
        print("you lose!")
        player_lives -= 1
    else:
        print("you win!")
        computer_lives -= 1

elif computer_choice == "paper":
    if player_choice == "scissors":
        print("you win!")
        computer_lives -= 1

    else:
        print("you lose!")
        player_lives -= 1
        
elif computer_choice == "scissors":
    if player_choice == "paper":
        print("you lose!")
        player_lives -= 1
    else: 
        print("you win!")  
        computer_lives -= 1

print("player lives:", player_lives)
print("computer lives:", computer_lives)
