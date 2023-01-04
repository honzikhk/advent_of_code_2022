# most size of directory: 100 000

def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        return format_data

data = read_data("day_7/test.txt")
# print(f"raw data: {data}")


def count_the_size_of_directories(formated_data):       # maybe delete this
    directories_size = {}
    only_names = []
    for command in formated_data:
        #name_of_directory = ""
        if command == "$ cd ..":
            continue
        elif command[0:4] == "$ cd":
            name_of_directory = command[5:]
            only_names.append(name_of_directory)
            directories_size[name_of_directory] = []
    return directories_size

directories_size = count_the_size_of_directories(data)
print(f"dicts of sizes: {directories_size}")


# def separate_directories(formated_data):
#     list_of_blocks = []
#     _ = []
#     for command in formated_data:
        
#         if command == "$ cd /":
#             continue
#         if command == "$ cd ..":
#             continue
        
#         if command[0:4] == "$ cd":
#             list_of_blocks.append(_.copy())
#             _.clear()
#             continue
#         _.append(command)
#     return list_of_blocks


def dummy_find_dirs(formated_data):
    all_dirrs = ["dir /"]
    for command in formated_data:
        if command[0:3] == "dir":
            all_dirrs.append(command)
    return all_dirrs

print(f"all dirrs finded by dommy function: {dummy_find_dirs(data)}")


def make_system(formated_data):
    """ Create dictionary of name of dir as a key and list of content as value """
    fucking_dictionary = {}
    for command in range(len(formated_data)):
        _ = []
        if formated_data[command][2:4] == "ls":
            for command_2 in range(command + 1, len(formated_data)):
                if formated_data[command_2][0] == "$":
                    break
                _.append(formated_data[command_2])
            fucking_dictionary[formated_data[command - 1][5]] = _
    return fucking_dictionary


system_in_dict = make_system(data)
print(f"result of make_system: {system_in_dict}")





