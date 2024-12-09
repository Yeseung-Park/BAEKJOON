import sys

N, K = map(int, input().split())

coins = [0]*N

for i in range(N):
    coins[i] = int(sys.stdin.readline())

result = 0

# 동전 구하기
# 큰 것부터 생각하자
for i in range(N-1, -1, -1):
    if K < coins[i]:    # 내야할 돈보다 더 큰 동전이면 패스
        continue
    result += K // coins[i]
    K %= coins[i]

print(result)