T = int(input())    # 테스트 케이스의 개수

for tc in range(T):
    M, N, x, y = map(int, input().split())
    # M:M 카잉 달력의 마지막 해

    i, j = 0, 0
    result = 0

    for k in range(1, M*N):
        if i < M:
            i += 1
        else:
            i = 1
        if j < N:
            j += 1
        else:
            j = 1
        if i == x and j == y:
            result = k
            break

    if result == 0:
        print(-1)
    else:
        print(result)