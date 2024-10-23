N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def DFS(i, j):
    island.append((i, j))
    visited[i][j] = 1
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[ni][nj]:
                continue
            if board[ni][nj] == 0:
                continue
            DFS(ni, nj)



# 섬 구분하기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[0]*M for _ in range(N)]
k = 0    # 각기 다른 섬을 각기 다른 숫자로 나타낼 것이다.
for i in range(N):
    for j in range(M):
        if visited[i][j] or board[i][j] == 0:
            continue
        k += 1
        island = []
        DFS(i, j)
        for i, j in island:
            board[i][j] = k

# 섬 사이 다리 길이 구하기
# 행과 열로 나누어서 구하자
# 행 먼저
for i in range(N):
    island_start = False    # 시작섬을 발견했는지 확인하는 변수
    bridge = 0    # 섬 사이의 다리 길이

print(board)