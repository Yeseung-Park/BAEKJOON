A = int(input())
B = int(input())
C = int(input())

temp = str(A * B * C)

num_dict = {
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
}

for s in temp:
    num_dict[s] += 1

for value in num_dict.values():
    print(value)