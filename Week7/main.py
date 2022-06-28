# doesn't work - it's a binary file
# word_file = open("test.docx")
# print(word_file.read())

import os.path
from datetime import datetime

name = "Eric"

for letter in name:
    print(f'unicode value for {letter} is {ord(letter)}')
    print(f'the next letter is {chr(ord(letter) + 1)}')

# if you aren't using windows, or aren't sure what OS someone is using
# lookup os.path.join
file_in_c_drive = open("c:\\test\\test.txt", 'w')
file_in_c_drive.write("Hi c drive file")
file_in_c_drive.close()


# be careful with file names being deleted
file_to_delete = input("enter the file name to delete")
os.remove(file_to_delete)




log_file = open("logfile.txt", 'a')

log_file.write(f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day} "
               f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} "
               f"- You ran the program\n")

log_file.close()

continue_buying = 'y'

while continue_buying == 'y':
    item = input("Welcome to our amazing vending machine, what do you want to buy?")

    if os.path.isfile(item):
        item_file = open(item)
        price = float(item_file.readline())
        quantity_available = int(item_file.readline())

        item_file.close()

        print(f"{item} costs: ${price:.2f} and there are {quantity_available} available")

        quantity_to_buy = quantity_available + 1

        while quantity_to_buy > quantity_available:
            quantity_to_buy = int(input(f"How many {item} do you want to buy?"))

        print(f"That will cost ${quantity_to_buy * price}")

        item_file = open(item, 'w')  # will erase the file it opens

        item_file.write(f"{price}\n")
        item_file.write(f'{quantity_available - quantity_to_buy}')

        item_file.close()

    else:
        print("sorry we don't sell that")

    continue_buying = input("Do you want to buy more? y/n")

skittles_file = open("skittles")
price = float(skittles_file.readline())
quantity_available = int(skittles_file.readline())

print(f"Skittles cost: ${price:.2f} and there are {quantity_available} available")

skittles_file.close()

quantity_to_buy = quantity_available + 1

while quantity_to_buy > quantity_available:
    quantity_to_buy = int(input("How many skittles packs do you want to buy?"))


print(f"That will cost ${quantity_to_buy*price}")


skittles_file = open("skittles", 'w') # will erase the file it opens

skittles_file.write(f"{price}\n")
skittles_file.write(f'{quantity_available - quantity_to_buy}')

skittles_file.close()

file_to_read = open("test.txt")

line_number = 1

for line in file_to_read:
    print(line_number, ":", line, end="")
    line_number += 1

file_to_read.close()

#
# first_line = file_to_read.readline()
# print(first_line, end="")
#
# second_line = file_to_read.readline()
# print(second_line, end="")
#
# third_line = file_to_read.readline()
# print(third_line, end="")
#
# fourth_line = file_to_read.readline()
# print(fourth_line, end="")
#
# fifth_line = file_to_read.readline()
# print(fifth_line, end="")

#contents = file_to_read.read() # risky if the file is large

#print(contents)