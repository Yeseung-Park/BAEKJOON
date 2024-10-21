N, M = map(int, input().split())

bucket = [0] * N

for i in range(1, N+1):
    bucket[i-1] = i

for _ in range(M):
    start, end = map(int, input().split())
    for i in range(start, (start+end)//2+1):
        bucket[i-1], bucket[start+end-i-1] = bucket[start+end-i-1], bucket[i-1]

print(*bucket)