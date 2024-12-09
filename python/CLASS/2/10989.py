import sys

N = int(sys.stdin.readline())

count = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i)+"\n")

# 완벽한 카운팅 정렬은 아니지만 어쨌든 카운팅 정렬
# 시간을 줄이기 위해 sys.stdin.readline까지 써야하다니...