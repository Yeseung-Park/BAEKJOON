N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

result = []    # 각 단지의 종류와 해당 단지의 집 수를 인덱스와 리스트 값으로 나타내보자

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def DFS(i, j):    # DFS
    global houses
    houses += 1
    visited[i][j] = 1
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 1:    # 갈 수 있는 곳이면
            DFS(ni, nj)

for i in range(N):
    for j in range(N):    # 모든 점을 출발점으로 해서 가볼까
        if arr[i][j] == 1 and visited[i][j] == 0:    # 단지의 일부이면서 방문하지 않은 곳이라면
            houses = 0
            DFS(i, j)    # 이걸 출발점으로 해서 DFS를 하고 단지를 구분짓자.
            result.append(houses)

result.sort()
print(len(result))
for house in result:
    print(house)
