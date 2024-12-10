import sys
sys.setrecursionlimit(10000)

N = int(input())

arr = [list(input()) for _ in range(N)]
arr_colorblind = [[0]*N for _ in range(N)]

# 적록색약이 아닌 사람부터 하자
visited = [[0]*N for _ in range(N)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
result1 = 0

def DFS(si, sj):
    visited[si][sj] = 1
    for k in range(4):
        ni, nj = si+di[k], sj+dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[si][sj] and visited[ni][nj] == 0:
            DFS(ni, nj)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:    # 방문하지 않은 곳이라면
            # 시작점으로 해서 DFS를 돌린다.
            DFS(i, j)
            result1 += 1

# 적록색약인 사람을 위해서 배열을 따로 만들어봅시다.

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr_colorblind[i][j] = 'R'
        else:
            arr_colorblind[i][j] = arr[i][j]

visited_colorblind = [[0]*N for _ in range(N)]
result2 = 0

def DFS_colorblind(si, sj):
    visited_colorblind[si][sj] = 1
    for k in range(4):
        ni, nj = si+di[k], sj+dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr_colorblind[ni][nj] == arr_colorblind[si][sj] and visited_colorblind[ni][nj] == 0:
            DFS_colorblind(ni, nj)

for i in range(N):
    for j in range(N):
        if visited_colorblind[i][j] == 0:    # 방문하지 않은 곳이라면
            # 시작점으로 해서 DFS를 돌린다.
            DFS_colorblind(i, j)
            result2 += 1

print(result1, result2)