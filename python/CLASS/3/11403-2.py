# 플로이드-와샬 알고리즘을 쓰면 시간이 훨씬 줄어든다.
# 플로이드-와샬 알고리즘
# 주어진 그래프에서 각 정점 간의 최단 경로를 구하는 알고리즘
# 모든 쌍의 최단 경로를 구할 수 있는 알고리즘
# 주로 가중치가 있는 그래프에서 사용된다.
# DP를 이용하여 각 정점 간의 최단 경로를 점차적으로 갱신하는 방법
# 중간 정점을 추가하면서 경로를 갱신
# 중간 정점을 다르게 하면서 i->k->j로 가는 경로 중 더 짧은 경로가 존재한다면 갱신하는 그런 방법
# 이를 변형하여 각 정점 간에 "경로가 있는지"만을 확인할 수 있다.

import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for k in range(N):    # 중간 정점을 매번 갱신하면서 있는지 확인
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
                break

for lst in arr:
    print(*lst)