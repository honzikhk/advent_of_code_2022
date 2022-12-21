"""
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was NGCMPJLHV.
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


def one_move(count_of_moves, from_stack, to_stack):
    """ Removing box from stack """  
    stack_of_moving_boxes = []
    for move in range(count_of_moves):
        stack_of_moving_boxes.append(stacks[from_stack].pop())

    """ Adding new box """
    stack_of_moving_boxes.reverse()
    stacks[to_stack].extend(stack_of_moving_boxes)


def make_movements(movements):
    for movement in movements:
        _ = extract_data(movement)
        moves = _[0]
        from_stack = _[1]
        to_stack = _[2]
        # for move in range(moves):
        one_move(moves, from_stack, to_stack)
    return stacks


def create_final_message(final_position_of_boxes):
    message = ""
    for key in final_position_of_boxes:
        message += final_position_of_boxes[key][-1]
    return message


new_stacks = make_movements(movements)
pp.pprint(new_stacks)
print(f"message: {create_final_message(new_stacks)}")