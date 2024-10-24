# 이 문제는 너무 못풀었다... 너무 못했다 진짜...
# 진짜 모든 것을 다 참고하고 푼 듯... 내 힘으로 푼 게 없다...

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

result = 1e9

for i in range(N-8+1):
    for j in range(M-8+1):
        new_board = [row[j:j+8] for row in board[i:i+8]]
        B_count, W_count = 0, 0
        for k in range(8):
            for l in range(8):
                # 왼쪽 위를 검정색으로 해서 칠할 때
                if (k % 2 == 0 and l % 2 == 0) or (k % 2 == 1 and l % 2 == 1):
                    if new_board[k][l] != 'B':
                        B_count += 1
                elif (k % 2 == 1 and l % 2 == 0) or (k % 2 == 0 and l % 2 == 1):
                    if new_board[k][l] != 'W':
                        B_count += 1
                # 왼쪽 위를 하얀색으로 해서 칠할 때
                if (k % 2 == 0 and l % 2 == 0) or (k % 2 == 1 and l % 2 == 1):
                    if new_board[k][l] != 'W':
                        W_count += 1
                elif (k % 2 == 1 and l % 2 == 0) or (k % 2 == 0 and l % 2 == 1):
                    if new_board[k][l] != 'B':
                        W_count += 1
        temp = min(B_count, W_count)
        result = min(result, temp)

print(result)
