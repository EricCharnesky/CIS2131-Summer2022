first_class_letter_grade = input("enter your letter grade for class #1")
second_class_letter_grade = input("enter your letter grade for class #2")
third_class_letter_grade = input("enter your letter grade for class #3")
print()
grade_point = 0

if first_class_letter_grade == "A":
    grade_point += 4

elif first_class_letter_grade == "A-":
    grade_point += 3.7

elif first_class_letter_grade == "B+":
    grade_point += 3.3

elif first_class_letter_grade == "B":
    grade_point += 3

elif first_class_letter_grade == "B-":
    grade_point += 2.7

elif first_class_letter_grade == "C+":
    grade_point += 2.3

elif first_class_letter_grade == "C":
    grade_point += 2

elif first_class_letter_grade == "C-":
    grade_point += 1.7

elif first_class_letter_grade == "D+":
    grade_point += 1.3

elif first_class_letter_grade == "D":
    grade_point += 1

# default case
else:
    grade_point += 0 # doesn't actually do anything now


if second_class_letter_grade == "A":
    grade_point += 4

elif second_class_letter_grade == "A-":
    grade_point += 3.7

elif second_class_letter_grade == "B+":
    grade_point += 3.3

elif second_class_letter_grade == "B":
    grade_point += 3

elif second_class_letter_grade == "B-":
    grade_point += 2.7

elif second_class_letter_grade == "C+":
    grade_point += 2.3

elif second_class_letter_grade == "C":
    grade_point += 2

elif second_class_letter_grade == "C-":
    grade_point += 1.7

elif second_class_letter_grade == "D+":
    grade_point += 1.3

elif second_class_letter_grade == "D":
    grade_point += 1

# default case
else:
    grade_point += 0 # doesn't actually do anything now


if third_class_letter_grade == "A":
    grade_point += 4

elif third_class_letter_grade == "A-":
    grade_point += 3.7

elif third_class_letter_grade == "B+":
    grade_point += 3.3

elif third_class_letter_grade == "B":
    grade_point += 3

elif third_class_letter_grade == "B-":
    grade_point += 2.7

elif third_class_letter_grade == "C+":
    grade_point += 2.3

elif third_class_letter_grade == "C":
    grade_point += 2

elif third_class_letter_grade == "C-":
    grade_point += 1.7

elif third_class_letter_grade == "D+":
    grade_point += 1.3

elif third_class_letter_grade == "D":
    grade_point += 1

# default case
else:
    grade_point += 0 # doesn't actually do anything now

print("Your total grade point is:", grade_point)
grade_point_average = grade_point / 3
print("Your total grade point is:", grade_point_average)

if grade_point_average == 4:
    print("Your GPA is an A")
elif grade_point_average >= 3.7:
    print("Your GPA is an A-")
elif grade_point_average >= 3.3:
    print("Your GPA is an B+")
elif grade_point_average >= 3:
    print("Your GPA is an B")
elif grade_point_average >= 2.7:
    print("Your GPA is an B-")
elif grade_point_average >= 2.3:
    print("Your GPA is an C+")
elif grade_point_average >= 2:
    print("Your GPA is an C")
elif grade_point_average >= 1.7:
    print("Your GPA is an C-")
elif grade_point_average >= 1.3:
    print("Your GPA is an D+")
elif grade_point_average >= 1:
    print("Your GPA is an D")
else:
    print("Your GPA is an F")

have_recent_late_payments = input("Do you have any recent late payments? (yes/no): ")
annual_income = int(input("Enter your annual income ( no $ ): "))

# and
# true and true == true
# true and false == false
# false and true == false
# false and false == false

if annual_income >= 250_000:
    print("Here's your loan!")
elif annual_income >= 40_000 and have_recent_late_payments == "no":
    print("here's your loan")
else:
    print("no loan for you")

are_you_bored = input("Are you bored? (yes/no)")
do_you_have_homework = input("Do you have homework? (yes/no)")

# or
# true or true == true
# true or false == true
# false or true == true
# false or false == false

if do_you_have_homework == "yes" or are_you_bored == "yes":
    print("Go practice python!")
else:
    print("carry on")

if 9 == 10:
    apples = "apples"

# short circuit evaluation
if True and apples:
    print("yes apples")
else:
    print("what is apples?")

# for numeric variables, anything not 0 is true
if grade_point_average:
    print("Yes, GPA")
else:
    print(" =( ")

x = 0
# programmers
x = x + 1 # =)

# math majors
x = x + 1 # =(

