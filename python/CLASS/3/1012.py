# DFS하면 될 것 같은데요?

import sys

T = int(input())

# 재귀가 너무 많이 일어나니까 stack으로 구현하자
def DFS(i, j):    # i, j: 시작하는 행과 열
    stack = [(i, j)]
    visited[i][j] = 1
    while stack:
        ti, tj = stack.pop()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and field[ni][nj] == 1:
                visited[ni][nj] = 1
                stack.append((ni, nj))


for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    field = [[0]*M for _ in range(N)]

    for _ in range(K):
        j, i = map(int, sys.stdin.readline().strip().split())
        field[i][j] = 1    # 배추 심기

    visited = [[0]*M for _ in range(N)]    # 방문 배열
    result = 0
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]    # 동서남북 델타배열

    for i in range(N):
        for j in range(M):    # 모든 지점을 시작점으로 해서 돌아보자
            if visited[i][j] == 0 and field[i][j] == 1:
                # 방문 안 한 배추에 대해서만 탐색하기
                DFS(i, j)
                result += 1

    print(result)