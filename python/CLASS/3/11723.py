import sys

M = int(sys.stdin.readline())

dictionary = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
              '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
              '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
              '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}

for _ in range(M):
    command = sys.stdin.readline().strip()
    if 'add' in command:    # add일 경우
        command_num = command.split()[1]
        dictionary[command_num] = 1
    elif 'check' in command:    # check일 경우
        command_num = command.split()[1]
        if dictionary[command_num] == 1:
            print(1)
        else:
            print(0)
    elif 'remove' in command:    # remove일 경우
        command_num = command.split()[1]
        dictionary[command_num] = 0
    elif 'toggle' in command:    # toggle일 경우
        command_num = command.split()[1]
        if dictionary[command_num] == 1:
            dictionary[command_num] = 0
        else:
            dictionary[command_num] = 1
    elif 'all' == command:    # all일 경우
        for key in dictionary.keys():
            dictionary[key] = 1
    elif 'empty' == command:    # empty일 경우
        for key in dictionary.keys():
            dictionary[key] = 0
