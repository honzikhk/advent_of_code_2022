"""
--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?

Your puzzle answer was 2803.
"""
test_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 19
test_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 23
test_3 = "nppdvjthqldpwncqszvftbrmjlhg" # 23
test_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 29
test_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 26


def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        return format_data[0]

data = read_data("day_6/6.1_day_input.txt")


def decoding_signal(data):
    for step in range(len(data) - 14):
        end_step = step + 14
        #print(step, end_step)
        if len(set(data[step:end_step])) == 14:
            return end_step
        else:
            continue


print(decoding_signal(data))