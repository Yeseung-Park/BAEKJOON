N, M = map(int, input().split())
# N: 바구니의 개수
# M: 공을 넣는 횟수

buckets = [0] * N

for _ in range(M):
    start, end, ball = map(int, input().split())
    start -= 1    # 인덱스 맞춰주기 위함
    for i in range(start, end):
        buckets[i] = ball

print(*buckets)