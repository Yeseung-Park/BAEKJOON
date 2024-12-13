# 아까 1로 만들기를 했으니까 이 문제는 스스로 해볼 수 있을 것이다!
import sys

N = int(input())
scores = [0]*(N+1)

for i in range(1, N+1):
    scores[i] = int(sys.stdin.readline())

dp = [0]*(N+1)    # dp 배열
# dp[i]는 i번째 계단을 밟았을 때 얻을 수 있는 최대 점수
dp[0] = (0, 0)
dp[1] = (scores[1], 1)
cont = 0    # 연속으로 몇 번을 갔는지 측정하는

# 연속된 세 개의 계단을 모두 밟아서는 안 된다.
for i in range(2, N+1):
    if dp[i-1][1] == 2:    # 2번 연속 갔다면
        dp[i] = (dp[i-2][0]+scores[i], 0)
    else:
        if dp[i-1][0]+scores[i] > dp[i-2][0]+scores[i]:
            dp[i] = (dp[i-1][0]+scores[i], dp[i-1][1]+1)
        else:
            dp[i] = (dp[i-2][0]+scores[i], 0)

print(dp[N][0])