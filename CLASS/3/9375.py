# 이것도 결국 지피티의 약간의 도움....

import sys

T = int(sys.stdin.readline().strip())

for tc in range(T):
    n = int(input())
    cloth_dict = {}
    for _ in range(n):
        cloth, type = sys.stdin.readline().strip().split()
        if type not in cloth_dict.keys():
            cloth_dict[type] = 1
        else:
            cloth_dict[type] += 1

    # 결국 모든 조합은 해당 옷을 입거나 말거나니까
    # 각 종류의 옷 수 + 1 끼리 곱하면 된다
    # + 1을 해주는 이유는 선택 안 하는 선택지도 추가했기 때문에
    # 아무것도 안 입는 경우는 빼야하므로 마지막에 -1
    result = 1
    for value in cloth_dict.values():
        result *= (value+1)

    print(result-1)