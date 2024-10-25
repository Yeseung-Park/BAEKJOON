# BFS를 하되 시작 정점을 방문하지 않은 모든 정점으로 해서 여러번 BFS를 돌려야겠다.
# 유기농 배추랑 비슷한 문제
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
adjL = [[] for _ in range(N+1)]

# 인접배열 만들기
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

visited = [0]*(N+1)

def BFS(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.popleft()
        for next in adjL[t]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = 1

result = 0

# 모든 점을 시작 정점으로 하여 BFS 돌려보기
for i in range(1, N+1):
    if visited[i]:    # 방문했다면
        continue
    BFS(i)
    result += 1

print(result)