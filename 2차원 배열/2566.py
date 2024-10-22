board = [list(map(int, input().split())) for _ in range(9)]

maximum = -1
result = [0, 0]

for i in range(9):
    for j in range(9):
        if board[i][j] > maximum:
            maximum = board[i][j]
            result[0], result[1] = i+1, j+1

print(maximum)
print(*result)