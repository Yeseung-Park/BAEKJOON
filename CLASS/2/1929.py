# 이것도 지피티한테 물어봤다...

M, N = map(int, input().split())

disjoint = [True] * (N+1)
disjoint[0] = disjoint[1] = False

for i in range(2, int(N**0.5)+1):
    if disjoint[i]:    # 소수이면
        for j in range(i*i, N+1, i):    # i의 배수들을 모두 false로 표시
            disjoint[j] = False

for i in range(M, N+1):
    if disjoint[i]:
        print(i)