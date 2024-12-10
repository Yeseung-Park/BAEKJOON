# 3차원!!
# 한 번 가는걸 하루가 지났다고 합시다.
# BFS인가?
from collections import deque

M, N, H = map(int, input().split())
tomatoes = [0]*H

# 일단 3차원으로 쌓여있는 토마토의
for i in range(0, H):
    temp = [list(map(int, input().split())) for _ in range(N)]
    tomatoes[i] = temp

for k in range(H):
    for i in range(M):
        for j in range(N):
            pass
print(tomatoes)