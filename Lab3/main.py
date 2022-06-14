import random
import math


# affirmations from https://bestofaffirmations.com/generator/
def affirmation_generator():
    number = random.randint(1, 5)
    if number == 1:
        print("The point of life is balance, not perfection.")
    elif number == 2:
        print("I am capable of overcoming anything.")
    elif number == 3:
        print("I always pick myself back up.")
    elif number == 4:
        print("Though these times are difficult, they are only a short phase of life.")
    else:
        print("All I need is within me right now.")

    #return None - redundant


def quadratic_equation_intercept_finder(a, b, c):
    # a = input() - just use the value passed
    determinant = b**2 - (4 * a * c)
    if determinant < 0:
        return "There are no intercepts"

    first_x_intercept = (-b + math.sqrt(determinant)) / (2 * a)
    second_x_intercept = (-b - math.sqrt(determinant)) / (2 * a)

    return "x intercepts of " + str(first_x_intercept) + " and " + str(second_x_intercept)
    # return (first_x_intercept, second_x_intercept)

affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()

result = quadratic_equation_intercept_finder(1, 0, -4)

print(result)
