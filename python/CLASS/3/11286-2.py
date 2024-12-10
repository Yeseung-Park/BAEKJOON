# 내장함수를 사용해서도 풀어보자

from heapq import heappop
from heapq import heappush
import sys

N = int(input())
heap = []

for _ in range(N):
    t = int(sys.stdin.readline())
    if t != 0:    # 0이 아니라면 삽입
        heappush(heap, (abs(t), t))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)