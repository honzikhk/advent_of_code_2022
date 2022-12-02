#


def calc_score(input):
    my_shape_score = {"X": 1, "Y": 2, "Z": 3}
    opponent_shape_score = {"A": 1, "B": 2, "C": 3}
    my_score = 0

    with open(input, "r") as file:
        data = file.readlines()

    for round in data:
        my_shape = int(my_shape_score[round[2]])
        opponent_shape = int(opponent_shape_score[round[0]])



    return my_score


print(calc_score("day_2/2.1_day_input.sql"))