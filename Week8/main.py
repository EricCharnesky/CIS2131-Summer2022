my_list = [1, 2, 3, 4, 6] # lists are mutable
my_tuple = (1, 2, 3, 4, 5) # tuples are immutable
my_dictionary = {1, 2, 3, 4, 5} # dictionary are mutable
# mappings - key, and associated value

print(my_dictionary)

gradebook = {}
gradebook['Eric'] = 100 # assign the key of Eric, the value of 100
gradebook['Jeb'] = 90
gradebook['Journey'] = 75

gradebook['Eric'] = 95 # updates the existing value associated with Eric
gradebook['eric'] = 100 # keys are case-sensitive
print(f"Eric's score: {gradebook['Eric']}")

del gradebook['Journey'] # deletes the entry

# there is no order guaranteed in dictionaries

for key in gradebook: # loops through every key
    print(f'key: {key} - associated value: {gradebook[key]}')

# tuples, but not lists, can be used as keys
gradebook[(1, 2, 3)] = [4, 5, 6]

print(gradebook)

for value in gradebook.values():
    print(value)

if 'eric' in gradebook:
    print("Eric is in the class")
else:
    print("not in the class")

if 95 in gradebook.values():
    print("someone has a 95?")
else:
    print("No one has a 95")

print("items in my list")
for item in my_list:
    print(item)
print(my_list)

print("items in my tuple")
for item in my_tuple:
    print(item)
print(my_tuple)

for index in range(len(my_list)):
    print(f'Index: {index} - value: {my_list[index]}')

my_list[1] = 42
# my_list[10] = 42 - only works with existing indexes

for index in range(len(my_tuple)):
    print(f'Index: {index} - value: {my_tuple[index]}')

# fails - tuples can't be changed
# my_tuple[1] = 42

print(my_list)

# don't add/remove from lists while iterating
# remove all evens - this doesn't work
# for value in my_list[]:
for value in my_list[:]: # slice of everything in the list - copy
    print(f'currently checking {value}')
    if value % 2 == 0:
        my_list.remove(value)

print(my_list)

my_list.append(50) # adds to the end

my_list.insert(1, 100) # insert at what index, what value

my_list.pop(0) # defaults to removing the last item

print(my_list)

# lists don't check the type
crazy_list = ['some string', 2.34, 1, [2, 4, 6, 8, "who do we appreciate?"]]

print(crazy_list)

board = [
    [' ', ' ', ' '], # row index 0
    [' ', ' ', ' '], # row index 1
    [' ', ' ', ' '] ] # row index 2

board[0][1] = 'x'

for row in board:
    print(row)

board[1][1] = 'o'

for row in board:
    print(row)

three_dimensional_list = [
    [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ],
    [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ],
    [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
]

def average_value_in_list(some_list):
    total = 0
    for value in some_list:
        total += value
    return total / len(some_list)

print(my_list)
print(f"average of my_list: {average_value_in_list(my_list)}")

first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = first_list # this is NOT a copy - shallow copy
fourth_list = second_list[:] # this IS a copy - not really a deep copy
combined_list = first_list + second_list
print(combined_list)
first_list[1] = 0 # doesn't affect the combined list - but DOES affect third
second_list[1] = 0
print(combined_list)
print(third_list)
print(fourth_list)

print(sorted(my_list)) # doesn't modify the original, it returns a sorted copy

print(f'before sorting: {my_list}')
my_list.sort() # modifies the list
print(f'after sorting: {my_list}')

print(board)
print("\n".join(str(row) for row in board)) # list comprehension