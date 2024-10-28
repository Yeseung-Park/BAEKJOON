import sys
sys.setrecursionlimit(360000)

N, M = map(int, input().split())

campus = [list(input()) for _ in range(N)]

# 먼저 도연이의 위치 찾기
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start_i = i
            start_j = j

# 도연이의 위치를 시작으로 DFS를 돌아봅시다.
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]    # 상하좌우 인접탐색

cnt_set = set()
visited = [[0]*M for _ in range(N)]
visited[start_i][start_j] = 1
# 방문배열도 만들어주고

def DFS(i, j):    # i와 j는 행과 열
    if campus[i][j] == 'P':
        cnt_set.add((i, j))
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < M and campus[ni][nj] != 'X' and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            DFS(ni, nj)
    return

DFS(start_i, start_j)

if len(cnt_set):
    print(len(cnt_set))
else:
    print('TT')