import sys
from collections import  deque

N, M = map(int, sys.stdin.readline().split())
friendship = [[] for _ in range(N+1)]    # 친구관계를 나타내는 인접배열

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    friendship[v1].append(v2)
    friendship[v2].append(v1)

result = 0    # 사람의 번호
minimum = 1e9    # 케빈 베이컨 최솟값

def BFS(start):
    visited = [-1]*(N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        t = queue.popleft()
        for next in friendship[t]:
            if visited[next] != -1:
                continue
            queue.append(next)
            visited[next] = visited[t]+1

    return visited



for i in range(1, N+1):
    temp = BFS(i)
    temp_sum = sum(temp[1::])
    if temp_sum < minimum:
        minimum = temp_sum
        result = i

print(result)