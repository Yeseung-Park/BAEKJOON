count_dict = {}

string = input()
small_string = string.upper()

for s in small_string:
    if s in count_dict.keys():
        count_dict[s] += 1
    else:
        count_dict[s] = 1

maximum = max(count_dict.values())
result = []

for key, value in count_dict.items():
    if value == maximum:
        result.append(key)

if len(result) > 1:
    print('?')
else:
    print(result[0])