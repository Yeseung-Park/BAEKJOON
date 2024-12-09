n = int(input())

result = 0

fact_dp = [0]*(1001)    # 1000까지의 팩토리얼 값을 담는 dp
fact_dp[1] = 1

for i in range(2, 1001):
    fact_dp[i] = fact_dp[i-1]*i

for i in range(n+1):
    for j in range(n+1//2+2):    # 10만번 돌아도 괜찮은가?
        if (i*1 + j*2) == n:    # 괜찮으면
            if i == 0:    # 2cm 짜리로만 만들어져 있으면
                result += 1
            elif j == 0:    # 1cm 짜리로만 만들어져 있으면
                result += 1
            else:
                # 같은 것이 있는 순열
                temp = int(fact_dp[i+j] // (fact_dp[i]*fact_dp[j]))
                result += temp

print(result % 10007)