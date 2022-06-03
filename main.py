import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input(
            "Pick an option between rock, paper or scissors: ").lower()

    print(f"\nPlayer({player}) : CPU({computer}).\n")

    if player == computer:
        print(f"\nPlayer({player}) : CPU({computer}). It's a Tie!\n")
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Bye")
    break
