


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