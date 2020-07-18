import random
# flow
# start up interaction
scoreboard = { "wins": 0, "losses": 0, "ties": 0 }
possible_choices = ["rock", "paper", "scissors"]
programs_choice = random.choice(possible_choices)

user_choice = input("Choose rock, paper, or scissors: ")
print(f'\nYou chose {user_choice} \n')
print(f'\nThe computer chose {programs_choice} \n')
# user will specify choice
# computer makes a choice
# compare
if user_choice == "rock":
    if programs_choice == "rock":
        print("its a tie")
        scoreboard["ties"]+=1
    elif programs_choice == "paper":
        print("You lose!")
        scoreboard["losses"]+-1
    else:
        print("You won!")
        scoreboard["wins"]+=1
elif user_choice == "scissors":
    if programs_choice == "rock":
        print("You lost!")
        scoreboard["ties"]+=1
    elif programs_choice == "paper":
        print("You won!")
        scoreboard["wins"]+-1
    else:
        print("You won!")
        scoreboard["wins"]+=1
elif user_choice == "paper":
    if programs_choice == "rock":
        print("You won!")
        scoreboard["wins"]+=1
    elif programs_choice == "paper":
        print("Its a tie!")
        scoreboard["ties"]+-1
    else:
        print("You lost!")
        scoreboard["losses"]+=1
else:
    print("please enter rock, paper or scissors")

print(f'\nScore {str(scoreboard)}')