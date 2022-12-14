"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was TDCHVHJTG.
"""
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
        if line[index_of_stack] == " ":
            continue
        else:
            _.append(line[index_of_stack])
    return _[::-1]          # reverse method returned None, so i used [::-1]


def build_stacks(list_of_indexes):
    """ Creates dictionary with keys 1 - 9, values will be empty lists"""
    stacks = {}
    for i in range(1, list_of_indexes[-1] + 1):         # [-1] stands for last(the highest) element in the list
        stacks[i] = []

    """ From each line takes the symbol of box. index 1, 5, 9 ... """
    index = 1
    for stack in range(1, max(stacks) + 1):
        stacks[stack] = build_one_stack(index)
        index += 4
    return stacks

pp.pprint(build_stacks(indexes_of_stacks))

def separate_movements(raw_data):
    """ Creates list of movements """
    data_movements = []
    for line in raw_data:
        if line.startswith("m"):
            data_movements.append(line)
    return data_movements



test_stacks = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
    }

test_movements = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]


stacks = build_stacks(indexes_of_stacks)        # dictionary
movements = separate_movements(data)            # list


def one_move(from_stack, to_stack):
    """ Removing box from stack """  
    box = stacks[from_stack].pop()

    """ Adding new box """
    stacks[to_stack].append(box)



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


def create_final_message(final_position_of_boxes):
    message = ""
    for key in final_position_of_boxes:
        message += final_position_of_boxes[key][-1]
    return message


new_stacks = make_movements(movements)
pp.pprint(new_stacks)
print(f"message: {create_final_message(new_stacks)}")
