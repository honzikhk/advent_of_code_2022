import pprint as pp

def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        return format_data

data = read_data("day_5/5.1_day_input.sql")


def count_stacks(data):
    """ Make list of numbers representing count of stacks. Start from 1 """
    for line in data:
        print(line)
        if line[1] == "1":
            list_of_numbers = line.split()
            list_of_integers = [int(number) for number in list_of_numbers]
            break
    return list_of_integers

indexes_of_stacks = count_stacks(data)
# print(f"indexes of stacks: {indexes_of_stacks}")


def separate_crates(data):
    crates = []
    for line in data:
        if line[1] == "1":
            break
        crates.append(line)
    return crates

crates = separate_crates(data)
# print(f"crates: {crates}")


def build_one_stack(index_of_stack):
    _ = []
    for line in crates:
        _.append(line[index_of_stack])
    return _


def build_stacks(list_of_indexes):
    """ Creates dictionary with keys 1 - 9, values will be empty lists"""
    stacks = {}
    for i in range(1, list_of_indexes[-1] + 1):         # [-1] stands for last(the highest) index in the list
        stacks[i] = []

    """ From each line takes the symbol of box. index 1, 5, 9 ... """
    index = 1
    for stack in range(1, max(stacks) + 1):
        stacks[stack] = build_one_stack(index)
        index += 4
    return stacks


def separate_movements(raw_data):
    """ Creates list of movements """
    data_movements = []
    for line in raw_data:
        if line.startswith("m"):
            data_movements.append(line)
    return data_movements



test_stacks = {
    1: [' ', 'N', 'Z'],
    2: ['D', 'C', 'M'],
    3: [' ', ' ', 'P']
    }

test_movements = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]


stacks = test_stacks# build_stacks(indexes_of_stacks)        # dictionary
movements = test_movements # separate_movements(data)            # list


def one_move(from_stack, to_stack):
    """ Removing box from stack """
    box = ""
    for position in stacks[from_stack]:

        if position != " ":
            box = position
            index = stacks[from_stack].index(position)
            stacks[from_stack][index] = " "
            break

    """ Adding new box """
    for i in range(len(stacks[to_stack])):
        if stacks[to_stack][i] != " ":
            index = i - 1
            stacks[to_stack][index] = box
            break       # new



def extract_data(line_of_move):
    lst = line_of_move.split()
    result = []
    for el in lst:
        try:
            result.append(int(el))
        except:
            continue
    if len(result) == 3:
        return result
    else:
        raise ValueError("Wrong number of commands")


def make_movements(movements):
    for movement in movements:
        _ = extract_data(movement)
        moves = _[0]
        from_stack = _[1]
        to_stack = _[2]
        for move in range(moves):
            one_move(from_stack, to_stack)
    return stacks

new_stacks = make_movements(movements)
pp.pprint(new_stacks)


# change the direction adding boxes to the list. so then i can just do .pop .append methods. Now i am limited the size of the list.
# so whne i add fourth element to the list, list just grow. now i go opposite direction to index 0. index 0 is limit for me


