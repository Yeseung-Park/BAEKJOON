fact_dp = [0]*1001
fact_dp[1] = 1

for i in range(2, 1001):
    fact_dp[i] = fact_dp[i-1] * i

n = int(input())
result = 0

for i in range(n+1):
    for j in range(n//2+2):
        if (i*1 + j*2) == n:
            if i == 0:    # 2cm로만 이루어진 경우
                result += 2**j
            elif j == 0:
                result += 1
            else:
                temp = int(fact_dp[i+j] // (fact_dp[i]*fact_dp[j]))
                result += temp*2**j

print(result % 10007)