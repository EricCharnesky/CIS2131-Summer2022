
def get_gradebook_line(student_name, percentage_score):
    return f"Name: {student_name} - Score: {percentage_score:.1f}"

def vowel_count(word):
    vowels = 0
    for character in word.lower():
        if character == "a" or character == "e" \
                or character == "i" or character == "o" \
                or character == "u":
            vowels += 1
    word = word.lower()
    vowels = word.count("a") \
        + word.count("e") \
        + word.count("i") \
        + word.count("o") \
        + word.count("u")

    return vowels


print(get_gradebook_line("Eric", 89.95))

# strings are IMMUTABLE - can't be changed in memory

name = input("Enter your name")

if " " in name:
    # taking a slice with [start_index : end_index not including ]
    index_of_space = name.find(" ")
    first_name = name[0:index_of_space]
    last_name = name[index_of_space+1:len(name)]
    print("First:", first_name)
    print("Last:", last_name)

    print(first_name, "<", last_name, ":", first_name < last_name)
    print(first_name, ">", last_name, ":", first_name > last_name)



for character in name:
    print(character)

for index in range(len(name)):
    # square braces meaning index of
    print(index, ":", name[index])

    # this crashses, you can't change characters inside a string
    #name[index] = name[index].upper()

print("Vowels in your name:", vowel_count(name))

if "eric" in name.lower():
    print("Hey, my name is Eric too!")

print(name)

print(name.lower())
print(name.upper())

name = name.lower() # makes a new string in memory
# name points at the new location in memory

name = name.replace("a", "x")
name = name.replace("e", "x")
name = name.replace("i", "x")
name = name.replace("o", "x")
name = name.replace("u", "x")

print(name.title())



email = ""

# not good validation
while (not (email.endswith(".com")
        or email.endswith(".net")
        or email.endswith(".edu"))) \
        or "@" not in email:
    # strip will remove leading and trailing white space
    email = input("Enter your email").strip()
    print("the at sign is in position", email.find('@'))

index_of_at_sign = email.find("@")

# slice defaults [ start_index = 0 : end_index = len(string) ]
print("id", email[:index_of_at_sign])
print("domain", email[index_of_at_sign+1:])

print(email[:])

# [ start_index : end_index : stride or step
print(email[::2], email[1::2])
print(email[::-1])

office_number = int(input("Enter your office room #"))


signature = "Name: " + name + "\n" \
    + "Email: " + email + "\n" \
    + "Office #" + str(office_number) + "\n" \
    + "Professor of Computer Information Systems"

signature = f'Name: {name}\n' \
    + f'Email: {email}\n' \
    + f'Office #{office_number}\n' \
    + "Professor of Computer Information Systems"

print(signature)
