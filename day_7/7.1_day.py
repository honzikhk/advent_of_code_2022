# most size of directory: 100 000

def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        return format_data

data = read_data("day_7/test.txt")
print(data)


def count_the_size_of_directories(formated_data):
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

print(count_the_size_of_directories(data))

def separate_directories(formated_data):
    list_of_blocks = []
    _ = []
    for command in formated_data:
        
        if command == "$ cd /":
            continue
        if command == "$ cd ..":
            continue
        
        if command[0:4] == "$ cd":
            list_of_blocks.append(_.copy())
            _.clear()
            continue
        _.append(command)
    return list_of_blocks


print(separate_directories(data))
