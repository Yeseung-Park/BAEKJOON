# 지금 이 문제의 특징은
# P(4) 부터 P(n-3)+P(n-2)의 값을 가지고 있다는 것이다.
# 따라서 피보나치 수열 때 썼었던 dp를 활용하면 되지 않을까?

T = int(input())

dp = [0, 1, 1, 1] + [0]*100

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for tc in range(T):
    N = int(input())
    print(dp[N])

