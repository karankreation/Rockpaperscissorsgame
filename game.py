


from random import randint
choices = ["rock", "paper", "scissors"]

#player_choice = choices[1] 

#print("index 1 in the choice array is " + player_choice+ ",which is paper")

player_choice = input("choose rock, paper, or scissors: ")
print("user chose: " + player_choice)

computer_choice = choices[randint(0, 2)]
print("computer chose: " + computer_choice)

if computer_choice == player_choice: 
    print("tie")
    
elif computer_choice == "rock":
    if player_choice == "scissors":
        print("you lose!")
    else:
        print("you win!")

elif computer_choice == "paper":
    if player_choice == "scissors":
        print("you win!")
    else:
        print("you lose!")
        
elif computer_choice == "scissors":
    if player_choice == "paper":
        print("you lose!")
    else: 
        print("you win!")