# 먼저 제일 긴 단어의 길이를 구하고 그걸 기준으로 2차원배열을 만들자.

maximum_length = 0
strings = []

for _ in range(5):
     string = input()
     strings.append(string)
     if len(string) > maximum_length:
         maximum_length = len(string)

board = [[0]*maximum_length for _ in range(5)]

for i in range(len(strings)):
    for j in range(len(strings[i])):
        board[i][j] = strings[i][j]

result = ''
for j in range(maximum_length):
    for i in range(5):
        if board[i][j] == 0:
            pass
        else:
            result += board[i][j]

print(result)