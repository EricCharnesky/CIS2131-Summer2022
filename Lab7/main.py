

def add_student(gradebook):
    name = input("enter the student name").lower()
    if name in gradebook:
        print(f'{name} is already in the gradebook')
    else:
        gradebook[name] = {}
        if len(gradebook) != 1:
            for assignment in gradebook[list(gradebook.keys())[0]]:
                score = int(input(f"enter the score for {name} for assignment {assignment}"))
                gradebook[name][assignment] = score


def add_assignment(gradebook):
    assignment_name = input("Enter the assignment name").lower()
    # assignment_total_points = int(input("how many points is the assignment worth?"))
    for student in gradebook:
        score = int(input(f"enter the score for {student}"))
        gradebook[student][assignment_name] = score


def print_average(gradebook):
    for student in gradebook:
        average = sum(gradebook[student].values()) / len(gradebook[student].values())
        print(f"{student} average score: {average}")


gradebook = {}
add_student(gradebook)
add_student(gradebook)
add_assignment(gradebook)
add_assignment(gradebook)
print_average(gradebook)
add_student(gradebook)
print(gradebook)