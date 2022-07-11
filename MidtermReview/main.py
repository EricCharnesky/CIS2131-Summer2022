import random


def midterm_function_question(first, middle, last):
    if first < middle and first > last:
        return last - first
    if middle < first and middle < last:
        return middle * 3
    if last < first and last < middle:
        return last * middle


print(midterm_function_question(1, 3, 5))
print(midterm_function_question(5, 3, 5))
print(midterm_function_question(5, 3, 1))
print(midterm_function_question(1, 3, 0))



total_score = 0

score = 0

# sentinel value
while score != -1:
    total_score += score
    score = int(input("Please enter a score or -1 to be all done"))

print("The total scores you entered are:", total_score)


total_score = 0
more_scores_to_enter = 'y'

while more_scores_to_enter.lower() == "y":
    total_score += int(input("Please enter a score"))
    more_scores_to_enter = input("DO you have more scores to enter? y/n")

print("The total scores you entered are:", total_score)


def vowel_count_sometimes_y(sentence):
    vowel_count = 0
    for letter in sentence.lower():
        #if letter == "a" or letter == "e" or letter == "i" or letter == ""...
        if letter in "aeiou":
            vowel_count += 1
        elif letter == 'y':
            if random.randint(1, 2) == 2:
                vowel_count += 1
    return vowel_count

print(vowel_count_sometimes_y("ERIC"))
print(vowel_count_sometimes_y("YYYYYY"))
print(vowel_count_sometimes_y("YYYYYY"))
print(vowel_count_sometimes_y("YYYYYY"))
print(vowel_count_sometimes_y("YYYYYY"))