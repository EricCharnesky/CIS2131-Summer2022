import random

ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

users_throw = int(input("enter: 1 for Rock, 2 for Paper, 3 for Scissors, "
                        "4 for Lizard, or 5 for Spock"))
computer_throw = random.randint(1, 5)

if users_throw == computer_throw:
    print("tie!")
elif (users_throw == ROCK and computer_throw == SCISSORS) or \
        (users_throw == ROCK and computer_throw == LIZARD) or \
        (users_throw == PAPER and computer_throw == ROCK) or \
        (users_throw == PAPER and computer_throw == SPOCK) or \
        (users_throw == SCISSORS and computer_throw == PAPER) or \
        (users_throw == SCISSORS and computer_throw == LIZARD) or \
        (users_throw == LIZARD and computer_throw == PAPER) or \
        (users_throw == LIZARD and computer_throw == SPOCK) or \
        (users_throw == SPOCK and computer_throw == SCISSORS) or \
        (users_throw == SPOCK and computer_throw == ROCK):
    print("You win!")
else:
    print("You lose!")
