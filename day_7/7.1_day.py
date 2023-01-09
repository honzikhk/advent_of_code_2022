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
# print(f"dicts of sizes: {directories_size}")


def dummy_find_dirs(formated_data):
    all_dirrs = ["dir /"]
    for command in formated_data:
        if command[0:3] == "dir":
            all_dirrs.append(command)
    return all_dirrs

list_of_directories = dummy_find_dirs(data)
print(f"all dirrs finded by dummy function: {list_of_directories}")


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


def sum_all_files(dictionary_system):
    dictionary_of_sums = {}
    for dir in dictionary_system:
        sum_of_sizes = 0
        list_of_content = []
        for file in dictionary_system[dir]:
            try:
                size_of_file = int(file.split()[0])
                sum_of_sizes += size_of_file
            except:
                list_of_content.append(file[4])
        list_of_content.append(sum_of_sizes)
        if len(list_of_content) == 1:
            dictionary_of_sums[dir] = list_of_content[0]
        else:
            dictionary_of_sums[dir] = list_of_content
    return dictionary_of_sums


counted_files = sum_all_files(system_in_dict)       # good
print(f"sum_all_files: {counted_files}")


def separate_counted_folders(dict_with_all_files_counted):
    dictionary_result = {}
    for part in dict_with_all_files_counted:
        if isinstance(dict_with_all_files_counted[part], int):
            dictionary_result[part] = dict_with_all_files_counted[part]
    return dictionary_result


only_sizes = separate_counted_folders(counted_files)
print(f"only sizes: {only_sizes}")

def reduce_known_dirs(dict_with_all_files_counted):
    for part in dict_with_all_files_counted:
        content = dict_with_all_files_counted[part]
        if isinstance(content, list):   #  and len(content) == 2
            new_content = []
            for each in content:
                if isinstance(each, str):
                    try:
                        new_content.append(content[each])
                    except:
                        new_content.append(each)
                else:
                    new_content.append(each)
            dict_with_all_files_counted[part] = new_content
        else:
            continue
    return




# only_sizes = {}

# def convert_dirs_to_sizes(dict_with_all_files_counted):
#     dictionary_result = {}
#     for part in dict_with_all_files_counted:
#         list_of_content = []
#         try:    
#             for file in dict_with_all_files_counted[part]:
#                 if isinstance(file, int):
#                     list_of_content.append(file)
#                 else:
#                     list_of_content.append(dict_with_all_files_counted[file])
#             dictionary_result[part] = list_of_content
#         except:
#             only_sizes[part] = dict_with_all_files_counted[part]
#     return dictionary_result

# print(f"coverted sizes: {convert_dirs_to_sizes(counted_files)}")
# print(f"only sizes: {only_sizes}")


# fix the problem with lists in result. maybe make two functions to sum sizes in lists...
# first sum directories that content only one sub-folder, then again, again...