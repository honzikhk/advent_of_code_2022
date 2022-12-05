

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

# print(read_data("day_4/test.sql"))

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
    for pair in read_data("day_4/test.sql"):
        full_ranges.append(make_numbers(pair))

    original_count_of_ranges = len(full_ranges)
    cnt = 0
    after_remove_duplicates = []
    for pair in full_ranges:
        _ = []
        for i in range(2):
            _.append(set)       # finish comparing two ranges and do something


    return full_ranges


print(count_same_ranges())