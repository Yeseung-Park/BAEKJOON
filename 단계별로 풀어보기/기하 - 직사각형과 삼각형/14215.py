a, b, c = map(int, input().split())

side_list = [a, b, c]
max_side = max(side_list)
max_side_idx = side_list.index(max_side)
another_side = []
for i in range(3):
    if i == max_side_idx:
        pass
    else:
        another_side.append(side_list[i])

while max_side >= sum(another_side):
    max_side -= 1

another_side.append(max_side)

print(sum(another_side))