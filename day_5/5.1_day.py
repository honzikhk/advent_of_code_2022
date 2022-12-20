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

test_data = {
    1: [' ', 'N', 'Z'],
    2: ['D', 'C', 'M'],
    3: [' ', ' ', 'P']
    }


stacks = build_stacks(indexes_of_stacks)
print("all stacks:")
pp.pprint(build_stacks(indexes_of_stacks))
