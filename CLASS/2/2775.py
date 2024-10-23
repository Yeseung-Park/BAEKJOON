T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())

    total = 0

    num_dict = {}    # 바로 아래층의 각 호별 사람들의 수를 저장하는 딕셔너리

    for i in range(0, k+1):
        people = 0
        for j in range(1, n+1):
            if j not in num_dict.keys():
                num_dict[j] = j
            else:
                people += num_dict[j]
                num_dict[j] = people

    print(num_dict[n])