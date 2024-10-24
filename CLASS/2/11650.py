import sys

N = int(input())

spots = [0]*N

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    spots[i] = (x, y)

spots.sort(key=lambda x: (x[0], x[1]))

for spot in spots:
    print(*spot)