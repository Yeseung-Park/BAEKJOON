import sys
from collections import  deque

N, M, V = map(int, sys.stdin.readline().strip().split())
adjL = [[] for _ in range(N+1)]

# 인접 배열 만들기
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

# 인접 배열 정렬하기
for array in adjL:
    array.sort()

# 스택으로 DFS 구현하는거 잘 기억하기!

def DFS(s, N):    # v: 시작 정점    N: 정점 개수
    visited = [0]*(N+1)
    stack = []
    path = [s]
    visited[s] = 1
    v = s    # v: 현재 위치해 있는 정점

    while True:
        for next in adjL[v]:    # v에 인접한 노드 중
            if visited[next] == 0:    # 방문하지 않았다면
                stack.append(v)    # 현재 위치를 push하고
                v = next    # 다음 정점으로 새로운 v로 지정 => 방문하겠다는 의미
                path.append(v)    # 방문 경로에 추가
                visited[v] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    return path

def BFS(s, N):
    queue = deque()
    visited = [0]*(N+1)
    queue.append(s)
    visited[s] = 1
    path = []

    while queue:
        t = queue.popleft()
        path.append(t)
        for next in adjL[t]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = 1

    return path

print(*DFS(V, N))
print(*BFS(V, N))