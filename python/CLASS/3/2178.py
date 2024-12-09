# 아 최단거리는 BFS를 해주는게 좋구나.
from collections import deque

N, M = map(int, input().split())    # 도착해야하는 지점
minimum = 1e9    # 결과가 될 최솟값

# 여기서 중요한 점은 배열은 0부터 시작이기 때문에 실질적으로 도착해야하는 지점은 N-1, M-1 이다.

maze = [list(map(int, input())) for _ in range(N)]    # 미로

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]    # 상하좌우 인접탐색을 위한 델타배열

visited = [[0]*M for _ in range(N)]    # 방문 확인 배열


# BFS를 해주자
def BFS(start_i, start_j):
    queue = deque()
    queue.append((start_i, start_j, 1))    # 시작 지점과 그때의 거리
    visited[start_i][start_j] = 1
    while queue:
        ti, tj, result = queue.popleft()
        if ti == N-1 and tj == M-1:    # 도착지에 도착했으면
            return result
        for k in range(4):    # 델타 탐색
            ni, nj = ti+di[k], tj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maze[ni][nj] != 0:
                queue.append((ni, nj, result+1))
                visited[ni][nj] = 1

result = BFS(0, 0)

print(result)