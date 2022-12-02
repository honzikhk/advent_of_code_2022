"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

Your puzzle answer was 207410.
"""


def calc_cal(input):
    cal_list = []
    sequence = []

    with open(input, "r") as file:
        data = file.readlines()
    for e in data:
        if e == "\n":
            cal_list.append(sequence)
            sequence = []
            continue
        sequence.append(int(e.replace("\n", "")))
    cal_list.append(sequence)       # add the last sequence

    sum_list = []
    for e in cal_list:
        sum_list.append(sum(e))
    sum_list.sort(reverse=True)
    return sum(sum_list[0:3])

print(calc_cal("day_1/1.1_day_input.sql"))