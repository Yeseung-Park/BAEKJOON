# 뭔가 최대힙과 최소힙을 둘 다 생각한 다음에 동시에 들어있는 숫자들을 생각하면 되려나 흠..
from heapq import heappop, heappush
import sys

T = int(input())

for _ in range(T):
    k = int(input())    # Q에 적용할 연산의 개수
    Q_max = []    # 최대힙
    Q_min = []    # 최소힙
    for _ in range(k):
        cal, num_temp = sys.stdin.readline().strip().split()
        num = int(num_temp)
        if cal == 'I':
            heappush(Q_max, -num)
            heappush(Q_min, num)
        else:
            # 음수로 집어넣어줬던 애들을 돌려줄 때가 왔다.
            Q_max_temp = list(map(lambda x: -x, Q_max))
            if not set(Q_max_temp).intersection(set(Q_min)):    # 빈 배열이라면
                pass
            else:
                if len(set(Q_max_temp).intersection(set(Q_min))) == 1:    # 하나만 들어있을 때는 최소 = 최대
                    heappop(Q_min)
                    heappop(Q_max)
                else:
                    if num == -1:
                        heappop(Q_min)
                    else:
                        heappop(Q_max)

    Q_max_final = list(map(lambda x: -x, Q_max))
    result_set = set(Q_max_final).intersection(set(Q_min))

    if result_set:
        print(max(result_set), min(result_set))
    else:
        print('EMPTY')
