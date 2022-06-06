import math

length = int(input("Enter the length of your fence"))
width = int(input("Enter the width of your fence"))

post_distance = int(input("How far apart are your posts going to be?"))

if length % post_distance or width % post_distance:
    print('Invalid spacing, please try again')
    quit()

number_of_posts = (length * 2 + width * 2) / post_distance

board_length = int(input("How long of a board are you going buy?"))

if board_length < post_distance:
    print("You need to buy longer boards, please try again")
    quit()

# integer division for whole number only - could also round down with math.floor
posts_covered_per_board = board_length // post_distance

# round up because you can't buy half a board
number_of_boards_required = math.ceil(number_of_posts / posts_covered_per_board)

boards_per_post = int(input("how many boards do you want to run across each post?"))

number_of_boards_required *= boards_per_post

cost_per_post = float(input("How much does each post cost?"))
cost_per_board = float(input("How much does each board cost?"))

total_post_cost = number_of_posts * cost_per_post
total_board_cost = number_of_boards_required * cost_per_board

grand_total = total_board_cost + total_post_cost

print("You need to buy", number_of_posts, "posts for $", total_post_cost)
print("You need to buy", number_of_boards_required, "boards for $", total_board_cost)
print("For a grand total of: $", grand_total)
