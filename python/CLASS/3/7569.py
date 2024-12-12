# 3차원!!
# 한 번 가는걸 하루가 지났다고 합시다.
# BFS인가?
from collections import deque
import sys

M, N, H = map(int, input().split())
tomatoes = [0]*H

# 일단 3차원으로 쌓여있는 토마토를 구현해야지
# 1: 익은 토마토 0: 익지 않은 토마토 -1: 토마토가 들어있지 않은 칸
for i in range(0, H):
    temp = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    tomatoes[i] = temp

di = [0, 0, -1, 1, 0, 0]
dj = [-1, 1, 0, 0, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

q = deque()

# BFS
def BFS(sk, si, sj, visited, times):
    q = deque()
    q.append((sk, si, sj))
    visited[sk][si][sj] = 0

    while q:
        tk, ti, tj = q.popleft()
        if times[tk][ti][tj] != 0:    # 전에 한 번 익는 시간이 측정되었는데
            if times[tk][ti][tj] >= visited[tk][ti][tj]:
                # 더 짧게 익는 시간이 존재한다면 갱신
                times[tk][ti][tj] = visited[tk][ti][tj]
        else:    # 처음 만나는 애라면 이게 일단 익는 시간
            times[tk][ti][tj] = visited[tk][ti][tj]
        for l in range(6):
            nk, ni, nj = tk+dk[l], ti+di[l], tj+dj[l]
            if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M:    # 인덱스 범위 안에 있고
                if visited[nk][ni][nj] == -1 and tomatoes[nk][ni][nj] == 0:    # 방문하지 않았고 익은 토마토도 아니면
                    visited[nk][ni][nj] = visited[tk][ti][tj] + 1
                    q.append((nk, ni, nj))

# 모든 익어있는 토마토를 시작으로 BFS를 돌되 매번 방문처리는 리셋해줘야 한다.
# 익는데에 걸리는 시간을 저장하는 배열은 또 따로 만들어줘야 한다.
# 매번 익어있는 토마토를 시작으로 BFS를 돌면 시간이 너무 오래 걸린다.
# 처음부터 deque에 익어있는 토마토를 넣어주면 어차피 거기를 시작으로 돌테니까...
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[k][i][j] == 1:    # 익은 토마토면 덱에 넣자
                q.append((k, i, j))

# 이렇게 기본 세팅된 덱을 가지고 BFS를 돈다.
while q:
    tk, ti, tj = q.popleft()
    for l in range(6):
        nk, ni, nj = tk+dk[l], ti+di[l], tj+dj[l]
        if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M:    # 인덱스 범위 안에 있고
            if tomatoes[nk][ni][nj] == 0:    # 방문하지 않았고 익은 토마토도 아니면
                tomatoes[nk][ni][nj] = tomatoes[tk][ti][tj] + 1
                q.append((nk, ni, nj))

# 일단 다 익을 수 있는지 없는지 알아봐야 한다.
# times를 한 번씩 돌면서 원래 -1이나 1이 아니었던 애들이 0이면 그건 결국 익지 못했다는 것이므로 결과로 -1을 출력
is_all_riped = True
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[k][i][j] == 0:
                is_all_riped = False
                break
        if not is_all_riped:
            break
    if not is_all_riped:
        break

if is_all_riped:
    result = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomatoes[k][i][j] > result:
                    result = tomatoes[k][i][j] - 1
    print(result)
else:
    print(-1)