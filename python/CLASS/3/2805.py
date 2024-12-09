# 최대한 높은 높이에서 잘라야한다.
import sys

N, M = map(int, sys.stdin.readline().strip().split())

trees = list(map(int, sys.stdin.readline().strip().split()))

# 이분탐색을 할까?
start = 1
end = max(trees)

while start <= end:
    middle = (start+end) // 2
    temp = 0    # 가져간 나무의 합
    for tree in trees:
        if middle < tree:
            temp += tree - middle
    if temp >= M:    # 더 많이 가져갈 수 있다면
        # 좀 더 높은 곳에서 잘라야 한다.
        start = middle + 1
    else:    # 더 적게 가져가게 된다면
        # 좀 더 낮은 곳에서 잘라야 한다.
        end = middle - 1

print(end)    # 근데 왜 end지?