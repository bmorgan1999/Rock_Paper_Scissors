import random


AI_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("that makes no sense, try again")
        Choose_Option()
    return user_choice

def AI_Option():
    AI_choice = random.randint(1,3)
    if AI_choice == 1:
        AI_choice = "r"
    elif AI_choice == 2:
        AI_choice = "p"
    else:
        AI_choice = "s"
    return AI_choice

while True:
    print("")
    user_choice = Choose_Option()
    AI_choice = AI_Option()
    print("")

    if user_choice == "r":
        if AI_choice == "r":
            print("You chose a rock. The AI chose a rock. You tied!")
        elif AI_choice == "p":
            print("You chose a rock. The AI chose paper. Loser!")
            AI_wins += 1

        elif AI_choice == "s":
            print("You chose a rock. The AI chose scissors. Winner, winner, chicken dinner!")
            player_wins += 1

    elif user_choice == "p":
        if AI_choice == "r":
            print("You chose paper. The AI chose a rock. Winner, winner, chicken dinner!")
            player_wins += 1

        elif AI_choice == "p":
            print("You chose paper. The AI chose paper. You tied!")

        elif AI_choice == "s":
            print("You chose paper. The AI chose sissors. Loser!")
            AI_wins += 1

    elif user_choice == "s":
        if AI_choice == "r":
            print("You chose scissors. The AI chose a rock. Loser!")
            AI_wins += 1

        elif AI_choice == "p":
            print("You chose scissors. The AI chose paper. Winner, winner, chicken dinner!")

        elif AI_choice == "s":
            print("You chose scissors. The AI chose scissors. You tied!")

    print("")
    print("Player wins: " + str(player_wins))
    print("AI wins: " + str(AI_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break












    
            





            
            
