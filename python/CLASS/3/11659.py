import sys

N, M = map(int, sys.stdin.readline().strip().split())

numbers = [0] + list(map(int, sys.stdin.readline().strip().split()))

dp = [0]*(N+1)    # 누적합?을 담는? 리스트?

for i in range(1, N+1):
    dp[i] = dp[i-1]+numbers[i]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    result = dp[end] - dp[start-1]
    print(result)

# 이건 정말 잘 풀었다 예승아