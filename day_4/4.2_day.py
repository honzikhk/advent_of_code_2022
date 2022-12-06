"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

Your puzzle answer was 801.
"""
def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        groups = [element.split() for element in format_data]       # first step of separation
        separated_ranges = [cell[0].split(",") for cell in groups]      # second step of separation

        integer_list = []
        for pair in separated_ranges:
            first = []
            for el in pair:
                second = []
                for symbol in el.split("-"):
                    second.append(int(symbol))
                first.append(second)
            integer_list.append(first)
        return integer_list


def make_numbers(list_of_sections): # [[2, 4], [6, 8]]
    start_range_1 = int(list_of_sections[0][0])
    end_range_1 = int(list_of_sections[0][1])

    start_range_2 = int(list_of_sections[1][0])
    end_range_2 = int(list_of_sections[1][1])

    first_range = []
    for i in range(start_range_1, end_range_1 + 1):
        first_range.append(i)

    second_range = []
    for i in range(start_range_2, end_range_2 + 1):
        second_range.append(i)

    return [first_range, second_range]


def count_same_ranges():
    full_ranges = []
    for pair in read_data("day_4/4.1_day_input.sql"):
        full_ranges.append(make_numbers(pair))

    cnt = 0
    for pair in full_ranges:
        """control if first range contains second range or opposite"""
        if not set(pair[0]).isdisjoint(set(pair[1])):       # if there is intersection, returns False
            cnt += 1
    return cnt


print(count_same_ranges())