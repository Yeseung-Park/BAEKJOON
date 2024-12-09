from heapq import heappop, heappush
import sys

N = int(input())    # 연산의 개수
heap = []
for _ in range(N):
    command = int(sys.stdin.readline().strip())
    if command == 0:    # 배열에서 가장 작은 값을 출력하고 제거
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:    # 그 외의 경우 배열에 추가
        heappush(heap, command)