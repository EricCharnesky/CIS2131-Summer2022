import os


def get_item_price_and_quantity(item_file_name):
    if os.path.exists(item_file_name):
        item_file = open(item_file_name)
        price = float(item_file.readline())
        quantity = int(item_file.readline())

        item_file.close()

        return price, quantity


def write_item_file(item_file_name, price, quantity):
    item_file = open(item_file_name, 'w')  # will erase the file it opens

    item_file.write(f"{price}\n")
    item_file.write(f'{quantity}')

    item_file.close()

def add_item(item_name):

    item_file_name = f'{item_name}.txt'

    if not os.path.exists(item_file_name):

        price = float(input("Please enter the item price"))
        quantity = int(input("Please enter the quantity of the item"))

        write_item_file(item_file_name, price, quantity)
    else:
        print("That item is already for sale, please update it instead")


def update_item(item_name):
    item_file_name = f'{item_name}.txt'

    if os.path.exists(item_file_name):

        price, quantity = get_item_price_and_quantity(item_file_name)

        print(f"{item_name} costs: ${price:.2f} and there are {quantity} available")

        price = float(input("Please enter the new item price"))
        quantity = int(input("Please enter the new quantity of the item"))

        write_item_file(item_file_name, price, quantity)

    else:
        print("That item is not for sale currently, please add it")


def remove_item(item_name):
    item_file_name = f'{item_name}.txt'

    if os.path.exists(item_file_name):
        os.remove(item_file_name)
    else:
        print("That item is not for sale currently")


mode = input("Do you want to Shop or Manage?").lower()

if mode == 'shop':

    # shop mode from https://github.com/EricCharnesky/CIS2131-Summer2022/blob/main/Week7/main.py
    continue_buying = 'y'

    while continue_buying == 'y':
        item = input("Welcome to our amazing vending machine, what do you want to buy?")
        item_file_name = f'{item}.txt'
        if os.path.isfile(item):
            price, quantity_available = get_item_price_and_quantity(item_file_name)

            print(f"{item} costs: ${price:.2f} and there are {quantity_available} available")

            quantity_to_buy = quantity_available + 1

            while quantity_to_buy > quantity_available:
                quantity_to_buy = int(input(f"How many {item} do you want to buy?"))

            print(f"That will cost ${quantity_to_buy * price}")

            write_item_file(f'{item}.txt', price, (quantity_available - quantity_to_buy))

        else:
            print("sorry we don't sell that")

        continue_buying = input("Do you want to buy more? y/n")

elif mode == 'manage':

    continue_managing = 'y'

    while continue_managing == 'y':

        choice = input("Do you want to Add an item, Update an item, or Remove an item?").lower()
        item_name = input("What is the item name you want to manage?")
        if choice == "add":
            add_item(item_name)
        elif choice == "update":
            update_item(item_name)
        elif choice == "remove":
            remove_item(item_name)
        else:
            print("I can't help with that")

        continue_managing = input("Do you want to manage more? y/n")