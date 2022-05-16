import math

my_favorite_number = 42

weight_of_my_kittens_in_kilograms = .35

# by default we get floating point results
print("7/2: ", 7 / 2)

# if you want a integer result
print("7//2: ", 7 // 2)

# to get a remiander, use modulus
print("7%2: ", 7 % 2)

people_attending_the_party = 13
average_number_of_pizza_rolls_eaten_per_person = 12
pizza_rolls_per_bag = 38

# \ tells python to keep reading the next line as if we didn't stop
total_pizza_rolls = people_attending_the_party * \
            average_number_of_pizza_rolls_eaten_per_person

bags_of_pizza_rolls_needed = total_pizza_rolls / pizza_rolls_per_bag
bags_of_pizza_rolls_needed = math.ceil(bags_of_pizza_rolls_needed)

print("You need to buy", bags_of_pizza_rolls_needed,
      "bags of pizza rolls for the party!")

print(1,000,000) # this is wrong and ugly
print(1, 000, 000) # this is wrong but pretty
print(1_000_000) # this is right and helpful
print(1_00_00_00) # this is legal, but wrong

name = "nana"
last_name = "batman!"
print(name*3, "batman!")

# string concatenation ( attaches with no spaces)
print(name + " " + last_name)
print(name, last_name)

students_enrolled = 24
students_attending_in_person = 16

# str converts something to a string
print(str(students_attending_in_person / students_enrolled * 100) +
      "% of students attend in person")
