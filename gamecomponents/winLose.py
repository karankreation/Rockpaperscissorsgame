
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