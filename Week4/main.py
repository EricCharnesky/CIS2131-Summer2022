import math
import random


def what_to_wear(weather):
    if weather == "sunny":
        return "sun screen"
    else:
        return "jacket"


# this is not correct
def citation_generator(title, author, publisher, year_published):
    print(author, title, year_published, publisher)


# optional / default parameters
def average_of_values(value1, value2=-1, value3=-1,
                      value4=-1, value5=-1, value6=-1, value7=-1):
    sum = value1
    count_of_values = 1

    if value2 != -1:
        sum += value2
        count_of_values += 1
    if value3 != -1:
        sum += value3
        count_of_values += 1
    if value4 != -1:
        sum += value4
        count_of_values += 1
    if value5 != -1:
        sum += value5
        count_of_values += 1
    if value6 != -1:
        sum += value6
        count_of_values += 1
    if value7 != -1:
        sum += value7
        count_of_values += 1

    result = sum / count_of_values

    return result

def bump_score_unless_greater_than_average(
        score, difference_from_100, average):
    if score > average:
        score += difference_from_100 / 2
    else:
        score += difference_from_100
    return score


# recursion - a method calling itself
def countdown(value):
    print(value)
    if value > 0:
        countdown(value-1)


def third(value):
    print(value)
    #first(value+1)


def second(value):
    print(value)
    third(value+1)


def first(value):
    print(value)
    second(value+1)


def sum_of_values(value1, value2):
    result = value1 + value2
    return result


def product_of_values(value1, value2):
    result = value1 * value2
    return result


def get_integer_input(prompt):
    value = int(input(prompt))
    return value


def rock_paper_scissors_lizard_spock_menu():
    print("Enter a number:")
    print("1 - Rock")
    print("2 - Scissors")
    print("3 - Paper")
    print("4 - Lizard")
    print("5 - Spock")
    choice = int(input())
    return choice


def determine_win_lose_draw(player_choice, computer_choice):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5

    if player_choice == computer_choice:
        print("Draw!")
    elif (player_choice == ROCK and computer_choice == SCISSORS) or \
            (player_choice == ROCK and computer_choice == LIZARD) or \
            (player_choice == PAPER and computer_choice == ROCK) or \
            (player_choice == PAPER and computer_choice == SPOCK) or \
            (player_choice == SCISSORS and computer_choice == PAPER) or \
            (player_choice == SCISSORS and computer_choice == LIZARD) or \
            (player_choice == LIZARD and computer_choice == PAPER) or \
            (player_choice == LIZARD and computer_choice == SPOCK) or \
            (player_choice == SPOCK and computer_choice == SCISSORS) or \
            (player_choice == SPOCK and computer_choice == ROCK):
        print("You win!")
    else:
        print("You lose!")


def get_random_computer_throw():
    return random.randint(1, 5)


# ** is the exponent operator

print("3^3 == ", 3**3)

print("4^4 == ", math.pow(4, 4))

# don't crash on sqrt of a negative
math.sqrt(-1)

author = input("Enter the author")
title = input("Enter the title")
publisher = input("Enter the publisher")
year = input("enter the year")

# named parameters - instead of giving them in order
# you tell python what order they are in
citation_generator(author=author, publisher=publisher,
                   year_published=year, title=title)

# you have to give required 'positional without defaults' arguments
average_of_values(value5=27, value1=10)


score_1 = int(input("Enter your 1st score 0-100"))
score_2 = int(input("Enter your 2nd score 0-100"))
score_3 = int(input("Enter your 3rd score 0-100"))

highest_score = score_1

if score_2 > highest_score:
    highest_score = score_2

if score_3 > highest_score:
    highest_score = score_3


average_score = average_of_values(score_1, score_2, score_3)
average_of_values(10, 20, 30, 40, 50, 60, 70)
average_of_values(10, 20, 30, 40)

difference_from_100 = 100 - highest_score

# assign the value returned, because when it is passed to the function
# it is passed as a copy
score_1 = bump_score_unless_greater_than_average(score_1, difference_from_100, average_score)
score_2 = bump_score_unless_greater_than_average(score_2, difference_from_100, average_score)
score_3 = bump_score_unless_greater_than_average(score_3, difference_from_100, average_score)

# # if the score is above the average, only give 1/2 the bump
# if score_3 > average_score:
#     score_3 += difference_from_100 / 2
# else:
#     score_3 += difference_from_100
#
# if score_2 > average_score:
#     score_2 += difference_from_100 / 2
# else:
#     score_2 += difference_from_100
#
# if score_1 > average_score:
#     score_1 += difference_from_100 / 2
# else:
#     score_1 += difference_from_100

print("Bumped score 1:", score_1)
print("Bumped score 2:", score_2)
print("Bumped score 3:", score_3)





countdown(10)



# int and input return values
length = get_integer_input("Enter the length")
width = get_integer_input("Enter the width")

# print doesn't return any values
result = print("test test test", "test again")

print(result)

player_choice = rock_paper_scissors_lizard_spock_menu()
computer_choice = get_random_computer_throw()
determine_win_lose_draw(player_choice, computer_choice)
determine_win_lose_draw("rock", "paper")

first(5)

print(sum_of_values(4, 2))
print(sum_of_values("apple", "banana"))
print(product_of_values(4, 2))
print(product_of_values("apple", 4))
print(product_of_values("apple", "banana"))

print(sum_of_values("apple", 2))



