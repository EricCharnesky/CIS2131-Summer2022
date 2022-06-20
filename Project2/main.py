import math
import random

MINIMUM_ROLL_TO_HIT = 12
MINIMUM_ROLL_TO_NEGOTIATE = 15
MINIMUM_ROLL_TO_FIND_TREASURE = 12
MINIMUM_ROLL_TO_NOT_GET_SICK = 10


def get_name():
    name = input("Enter your chacter's name: ")
    return name


def sum_of_four_six_sided_dice_with_lowest_dropped():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)

    sum = die1 + die2 + die3 + die4

    sum -= min(die1, die2, die3, die4)

    return sum


def menu():

    choice = ""

    # validation loop was extra for fun
    while choice != "attack" and choice != "negotiate" \
            and choice != "search" and choice != "eat":
        print("What do you want to do?")
        print("attack")
        print("negotiate")
        print("search")
        print("eat")
        choice = input()

    return choice


def get_ability_modifier(score):
    return math.floor(score - 10 / 2)


def attack(modifier, name):
    if random.randint(1, 20) + modifier >= MINIMUM_ROLL_TO_HIT:
        damage = random.randint(1, 6) + modifier
        if damage < 0:
            damage = 0
        print(name, "hits and deals", damage, "damage!")
    else:
        print(name, " misses!")


def negotiate(modifier, name):
    if random.randint(1, 20) + modifier >= MINIMUM_ROLL_TO_NEGOTIATE:
        print(name, "negotiates a truce!")
    else:
        print(name, "failed to negotiate!")


def get_random_treasure_name():
    value = random.randint(1, 4)

    if value == 1:
        return "gems"
    if value == 2:
        return "jade statue"
    if value == 3:
        return "gold"
    if value == 4:
        return "other type of treasure"
    return "laptop"


def search(modifier, name):
    if random.randint(1, 20) + modifier >= MINIMUM_ROLL_TO_FIND_TREASURE:
        print(name, "finds a", get_random_treasure_name())
    else:
        print(name, "didn't find anything!")


def eat(modifier, name):
    print(name, "ate some rancid food", end=" ")
    if random.randint(1, 20) + modifier >= MINIMUM_ROLL_TO_NOT_GET_SICK:
        print("but are ok")
    else:
        print("and got sick, you need to stay in bed")


name = get_name()
strength = sum_of_four_six_sided_dice_with_lowest_dropped()
dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
charisma = sum_of_four_six_sided_dice_with_lowest_dropped()

for turn in range(4):
    choice = menu()
    if choice == "attack":
        better_modifier = max(get_ability_modifier(strength),
                              get_ability_modifier(dexterity))
        attack(better_modifier, name)
    elif choice == "negotiate":
        negotiate(get_ability_modifier(charisma), name)
    elif choice == "search":
        better_modifier = max(get_ability_modifier(intelligence),
                              get_ability_modifier(wisdom))
        search(better_modifier, name)
    elif choice == "eat":
        eat(get_ability_modifier(constitution), name)
