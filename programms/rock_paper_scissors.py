import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)


while True:

    player = None
    while player not in choices:
        player = input("Was wählst du? ").lower()

    if(player == computer):
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Player won!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Computer won!")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Player won!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Computer won!")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Player won!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Computer won!")

    play_again = input("Nochmal spielen? (ja/nein): ").lower()

    if play_again != "ja":
        break
print("game Over!")