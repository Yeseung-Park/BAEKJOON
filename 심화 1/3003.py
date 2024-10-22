pieces = list(map(int, input().split()))
result = [0]*6
for i in range(len(pieces)):
    if i in [0, 1]:
        if pieces[i] != 1:
            result[i] = 1-pieces[i]
    elif i in [2, 3, 4]:
        if pieces[i] != 2:
            result[i] = 2-pieces[i]
    else:
        if pieces[i] != 8:
            result[i] = 8-pieces[i]

print(*result)