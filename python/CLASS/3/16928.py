from collections import deque

N, M = map(int, input().split())

# u칸에 갔을 때 v칸으로 이동한다는 걸 딕셔너리로 표현해볼까?
move_dict = {}

for _ in range(N):
    u, v = map(int, input().split())
    move_dict[u] = v
for _ in range(M):
    u, v = map(int, input().split())
    move_dict[u] = v

# 이번에도 BFS를 쓰되 visited를 한 번 더 써봅시다.

visited = [-1]*101    # 칸 번호랑 인덱스 번호를 맞춰주기 위함

def BFS(s):
    q = deque()
    visited[s] = 0
    q.append(s)

    while q:
        ti = q.popleft()
        for k in range(1, 7):
            if ti+k > 100:    # 100보다 커지면
                continue    # 갈 수 없다
            if ti+k in move_dict:    # 뱀이나 사다리를 만나면 이동!!
                next = move_dict[ti+k]
            else:
                next = ti+k
            if visited[next] == -1:    # 방문한 적이 없다면
                visited[next] = visited[ti] + 1
                q.append(next)

    return visited[100]

result = BFS(1)

print(result)