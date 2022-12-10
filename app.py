import random

rounds = 0
while rounds < 3:
    RoPaSc = input("choose rock, paper, or scissors: \n")
    choices = ["rock", "paper", "scissors"]
    comInput = random.choice(choices)

    if RoPaSc == comInput:
        if comInput == RoPaSc:
            print(f"You have both chosen {RoPaSc} \n")
    elif comInput == "rock":
        if RoPaSc == "paper":
            print("Paper beats rock, you win!\n")
    elif comInput == "paper":
        if RoPaSc == "rock":
            print("Paper beats rock, you lose!\n")
    elif comInput == "paper":
        if RoPaSc == "scissors":
            print("Paper beats scissors, you win!\n")
    elif comInput == "scissors":
        if RoPaSc == "paper":
            print("Scissors beats paper, you lose!\n")
    elif comInput == "rock":
        if RoPaSc == "scissors":
            print("Rock beats scissors, you lose!\n")
    elif comInput == "scissors":
        if RoPaSc == "rock":
            print("Rock beats scissors, you win!\n")
    else:
        exit(0);

    rematch = input("Would you like a rematch? (yes/no): \n")
    if rematch.lower() != "yes":
        rounds += 1
        break
    elif rematch.lower() == "no":
        exit(0);

print("\n\n")