import random


# lists are better for this, but we aren't there yet
def prompt_for_rock_paper_scissors_lizard_or_spock():
    choice = ""
    while choice != "rock" and choice != "paper" \
            and choice != "scissors" and choice != "lizard" \
            and choice != "spock":
        choice = input("What do you throw? Rock, Paper, Scissors, Lizard or Spock?").lower()
    return choice


def get_int_between_values(min_value, max_value, prompt="Please enter a number between "):
    value = min_value - 1 # start at invalid, so the loop runs
    while value < min_value or value > max_value:
        value = int(input(prompt + str(min_value) + "-" + str(max_value)))
    return value


# nested loops
for tens_place in range(10): # 0-9
    for ones_place in range(10): # 0-9
        print( tens_place * 10 + ones_place)


receipt_running_total = 0

receipt = -1

while receipt != 0: # sentinel value - unusual value - used to indicate the end of the loop
    receipt = float(input("Enter the receipt value or 0 to stop"))
    receipt_running_total += receipt

print("Total receipts: $" + str(receipt_running_total))


ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

number_of_rolls = 100
for roll in range(number_of_rolls):
    number = random.randint(1, 6)
    print("roll # " + str(roll) + ": " + str(number))
    if number == 1:
        ones += 1
    elif number == 2:
        twos += 1
    elif number == 3:
       # continue # jump back to the top
        threes += 1
    elif number == 4:
        fours += 1
    elif number == 5:
        fives += 1
    elif number == 6:
        sixes += 1
        # break # ENDS the loop

print("Ones:\t" + "*" * ones)
print("Twos:\t" + "*" * twos)
print("Threes:\t" + "*" * threes)
print("Fours:\t" + "*" * fours)
print("Fives:\t" + "*" * fives)
print("Sixes:\t" + "*" * sixes)

print("Ones:\t" + str(ones / number_of_rolls))
print("Twos:\t" + str(twos / number_of_rolls))
print("Threes:\t" + str(threes / number_of_rolls))
print("Fours:\t" + str(fours / number_of_rolls))
print("Fives:\t" + str(fives / number_of_rolls))
print("Sixes:\t" + str(sixes / number_of_rolls))


size = int(input("What size triangle do you want?"))
# left aligned
for row in range(size):
    print("*" * (row+1))

# right aligned
for row in range(size):
    number_of_spaces = size - row - 1
    print(" " * number_of_spaces + "*" * (row+1))

#     *
#    **
#   ***
#  ****
# *****

# check for odd
if size % 2 == 0:
    size += 1


number_of_stars = 1
number_of_spaces = size // 2

while number_of_stars <= size:
    print(" " * number_of_spaces + "*" * number_of_stars)
    number_of_stars += 2
    number_of_spaces -= 1


#     *
#    ***
#   *****
#  *******
# *********

# size | spaces
#   5  |   2
#   7  |   3
#   9  |   4
#
#

height = int(input("Enter the height rectangle you want to print"))
width = int(input("Enter the width rectangle you want to print"))

for row in range(height):
    print("*" * width)

# for loops run once for each item in a collection
for value in range(10): # gives you values 0-9 - up to but not including the value given
    print(value)



value = int(input("Enter a value to count down from"))
while value > 0:
    print(value)
    value -= 1
print("blast off!")


while True: # this is really lazy
    print(value)
    value += 1
    if value == 10: # if you know it here, use it above
        break # ends the loop

while value != 20:
    print(value)
    value += 1

another_value = get_int_between_values(1, 100)

# validation loop
# while condition checks for invalid values
while another_value < 1 or another_value > 100:
    print("That's not 1-100, try again")
    another_value = get_int_between_values(1, 100)


another_value_times_9 = another_value * 9

print("Your value * 9 is", another_value_times_9)

sum_of_digits = 10 # dummy value ensuring it runs at least once
while sum_of_digits >= 10:

    hundreds_place = another_value_times_9 // 100
    tens_place = another_value_times_9 % 100 // 10
    ones_place = another_value_times_9 % 10
    sum_of_digits = hundreds_place + tens_place + ones_place

    print("The hundreds place is", hundreds_place)
    print("The tens place is", tens_place)
    print("The ones place is", ones_place)
    print("The sum of the ones and tens place is: ", sum_of_digits)
    another_value_times_9 = sum_of_digits




top_value = int(input("How high of a number do you want to guess to?"))

magic_number = random.randint(1, top_value)
number_of_guesses = 1
guess = get_int_between_values(1, top_value, "Guess a number between ")

# if the while condition is true, the whole block of code runs
while guess != magic_number: # if this is false, the loops ends/doesn't run
    if guess < magic_number:
        print("Too low")
    else:
        print("Too High")
    guess = get_int_between_values(1, top_value, "Guess again! ")
    number_of_guesses += 1
    # when python gets here, it goes back and checks the condition

print("you guessed it in", number_of_guesses, "guesses!")