# 이건 했던거네 그냥 2차원 더 쉬운데
import sys
from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
q = deque()
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            q.append((i, j))

while q:
    ti, tj = q.popleft()
    for k in range(4):
        ni, nj = ti+di[k], tj+dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if tomatoes[ni][nj] == 0:
                q.append((ni, nj))
                tomatoes[ni][nj] = tomatoes[ti][tj] + 1

is_all_riped = True
result = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            is_all_riped = False
            print(-1)
            break
        else:
            if tomatoes[i][j] > result:
                result = tomatoes[i][j]
    if not is_all_riped:
        break

if is_all_riped:
    print(result-1)