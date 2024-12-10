from collections import deque
import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]    # 인접행렬
answer = [[0]*N for _ in range(N)]

# BFS를 해줘볼까
def BFS(i):
    q = deque()
    visited = [0]*N
    q.append(i)

    while q:
        ti = q.popleft()
        path.append(ti)
        for k in range(N):
            if visited[k] == 0 and arr[ti][k] == 1:    # 갈 수 있는 곳이라면
                visited[k] = 1
                q.append(k)

for i in range(N):
    for j in range(N):
        path = []
        BFS(i)
        if i == j:
            if j in path[1::]:
                answer[i][j] = 1
        else:
            if j in path:
                answer[i][j] = 1

for lst in answer:
    print(*lst)