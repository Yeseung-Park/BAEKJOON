# 모든 점을 시작으로 4번만 DFS를 해볼까
# 이번에도 시간초과 날 것 같지만...
# 근데 ㅗ자 블록은 어떻게 하지
# 진짜 ㅗㅗㅗㅗㅗㅗ
# 대각선도 가능하게 하면 너무 오래 걸릴 것 같은데...
# ㅗ자 블록은 우선 따로 해볼까
import sys

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
result = 0    # 최종 결과
visited = [[0]*M for _ in range(N)]

def DFS(i, j, num, temp):    # i, j: 현재 좌표 num: DFS 횟수 temp: 현재까지의 합
    global result
    if num == 4:    # 4칸 다 돌았으면
        result = max(result, temp)
        return
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            DFS(ni, nj, num+1, temp+numbers[ni][nj])
            visited[ni][nj] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, 1, numbers[i][j])
        visited[i][j] = 0

# 이번에는 ㅗ자 블록만 따로 해보자.
# 세 칸 일자 블록에 가운데 블록의 위 아래 둘 중에 하나를 더하는거지
# 가로 방향 세로 방향 따로 하자
# 먼저 가로 방향
for i in range(N):
    for j in range(M-2):
        temp = numbers[i][j] + numbers[i][j+1] + numbers[i][j+2]
        if 0 <= i+1 < N:
            temp += numbers[i+1][j+1]
            result = max(result, temp)
            temp -= numbers[i+1][j+1]
        if 0 <= i-1 < N:
            temp += numbers[i-1][j+1]
            result = max(result, temp)
            temp -= numbers[i-1][j+1]
# 이제 세로 방향
for j in range(M):
    for i in range(N-2):
        temp = numbers[i][j] + numbers[i+1][j] + numbers[i+2][j]
        if 0 <= j+1 < M:
            temp += numbers[i+1][j+1]
            result = max(result, temp)
            temp -= numbers[i+1][j+1]
        if 0 <= j-1 < M:
            temp += numbers[i+1][j-1]
            result = max(result, temp)
            temp -= numbers[i+1][j-1]

print(result)