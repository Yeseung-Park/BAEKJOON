# 경우는 크게 두 가지로 나눌 수 있다.
# 어차피 동생은 움직이지 않으니까
# 수빈이보다 동생이 뒤에 있는 경우
# 수빈이보다 동생이 앞에 있는 경우

import sys
sys.setrecursionlimit(100000)
from collections import deque

N, K = map(int, input().split())    # N: 수빈의 위치    K: 동생의 위치

# 재귀를 도는데 수빈의 현재 위치를 인자로 보내자.
# 몇 번 움직였는지도 인자로 보내자.
# 재귀 순서는 앞으로 1 이동, 뒤로 1 이동, 순간이동 순으로 진행

visited = [0]*100001

def BFS(start):
    queue = deque()
    visited = [-1]*100001
    queue.append(start)
    visited[start] = 0

    while queue:
        t = queue.popleft()
        if t == K:
            return visited[t]
        for next in [t+1, t-1, t*2]:
            if 0 <= next <= 100000 and visited[next] == -1:
                queue.append(next)
                visited[next] = visited[t]+1

result = BFS(N)

print(result)