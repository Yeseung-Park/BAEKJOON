string = input()
result = 0

for s in string:
    if s in ['A', 'B', 'C']:
        result += 3
    elif s in ['D', 'E', 'F']:
        result += 4
    elif s in ['G', 'H', 'I']:
        result += 5
    elif s in ['J', 'K', 'L']:
        result += 6
    elif s in ['M', 'N', 'O']:
        result += 7
    elif s in ['P', 'Q', 'R', 'S']:
        result += 8
    elif s in ['T', 'U', 'V']:
        result += 9
    else:
        result += 10

print(result)