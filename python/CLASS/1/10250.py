# 왼쪽 아래부터 위쪽으로 차례대로 채우면 되겠네

T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    find_room = False
    for i in range(1, W+1):
        for j in range(1, H+1):
            cnt += 1
            if cnt == N:
                find_room = True
                floor = j
                number = i
                break
        if find_room:
            break

    if number <= 9:    # 한자리수라면
        result = str(floor) + '0' + str(number)
    else:
        result = str(floor) + str(number)

    print(result)