N, M = map(int, input().split())

bucket = [0] * N    # 바구니
for i in range(N):
    bucket[i] = i+1    # 바구니 초기 설정

for _ in range(M):
    ball1, ball2 = map(int, input().split())
    bucket[ball1-1], bucket[ball2-1] = bucket[ball2-1], bucket[ball1-1]

print(*bucket)