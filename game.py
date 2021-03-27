


from random import randint
from gamecomponents import gameVars


def winorlose(status):
    #print("inside winorlose function; status is: ",status)
    print("You", status, "! Would you like to play again?")
    choice = input("Y / N? ")

    if choice == "N" or choice == "n":
        print("you chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":

        gameVars.player_lives = gameVars.total_lives
        gameVars.computer_lives = gameVars.total_lives
    else:
        print("Make a valid choice - Y or N")
        choice = input("Y / N?")

while gameVars.player_choice is False:
    print("=======================*/ RPS GAME */=======================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("============================================================")

    print("Choose your weapon! Or type quit to exit\n")

    gameVars.player_choice = input("choose rock, paper, or scissors: \n ")

    if gameVars.player_choice == "quit":
        print("You chose to quit")
        exit()

        
    print("user chose: " + gameVars.player_choice)

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice: 
        print("tie")
        
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print("you lose!")
            gameVars.player_lives -= 1
        else:
            print("you win!")
            gameVars.computer_lives -= 1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print("you win!")
            gameVars.computer_lives -= 1

        else:
            print("you lose!")
            gameVars.player_lives -= 1
            
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            print("you lose!")
            gameVars.player_lives -= 1
        else: 
            print("you win!")  
            gameVars.computer_lives -= 1
    
   
    if gameVars.player_lives == 0:
        winorlose("lose")
    
    if gameVars.computer_lives == 0:
        winorlose("won")
        
    
    print("player lives:", gameVars.player_lives)
    print("computer lives:", gameVars.computer_lives)


    gameVars.player_choice = False