import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
answer = [[0]*m for _ in range(n)]

#우선 BFS로 일단 풀어볼까 최단거리니까 최소비용이 아니라
# 역시 시간 초과가 나오는군...
# 그러면 뭘로 접근해야할까
# 아 BFS는 어차피 모든 지점을 한 번씩 다 도니까 그냥 BFS를 한 번만 해주면 되겠구나
# visited 배열을 적당히 다르게 배정해주면 최단거리를 알 수 있다!
# 이건 배웠던건데 까먹었네... 잘 기억해두자 진짜...

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS(si, sj):    # si, sj는 시작 좌표
    find_end = False
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0

    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1 and arr[ni][nj] == 1:
                # 갈 수 있는 곳이면
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1

    return visited

# 먼저 시작점을 찾아봅시다.
find_start = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            si, sj = i, j
            find_start = True
            break
    if find_start:
        break

result = BFS(si, sj)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            continue
        answer[i][j] = result[i][j]

for lst in answer:
    print(*lst)