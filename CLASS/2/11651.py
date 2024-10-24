# 11650이랑 거의 똑같은 문제 아니야?

import sys

N = int(input())

spots = [0]*N

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    spots[i] = (x, y)

spots.sort(key=lambda x: (x[1], x[0]))

for spot in spots:
    print(*spot)