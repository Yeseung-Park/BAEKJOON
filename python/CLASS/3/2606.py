# BFS하자

from collections import deque

V = int(input())    # 컴퓨터의 수
E = int(input())    # 연결 쌍의 수
adjL = [[] for _ in range(V+1)]    # 번호와 인덱스를 일치시키기 위한 V+1

# 인접 배열 만들기
for _ in range(E):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

def BFS(v):    # v: 시작 번호
    q = deque()
    visited = [0]*(V+1)
    q.append(v)
    visited[v] = 1
    # push하면 방문 처리
    result = 0   # 방문한 컴퓨터의 수

    while q:
        t = q.popleft()
        result += 1
        for next in adjL[t]:
            if visited[next]:    # 방문했으면
                continue
            q.append(next)
            visited[next] = 1

    return result

print(BFS(1)-1)