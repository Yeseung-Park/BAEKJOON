from heapq import heappop, heappush
import sys

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    command = int(sys.stdin.readline().strip())
    if command == 0:    # pop
        if heap:    # 배열이 채워져있는 상태이면
            print(heappop(heap)*(-1))
        else:
            print(0)
    else:    # push
        heappush(heap, command*(-1))