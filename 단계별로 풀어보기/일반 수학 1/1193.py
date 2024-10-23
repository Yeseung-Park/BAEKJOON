X = int(input())

turn = 0
k = 0
find_fraction = False

while True:
    if k % 2 == 0:    # 짝수일 경우
        # 왼쪽 아래에서 오른쪽 위로 올라가야 한다.
        for i in range(k, -1, -1):
            turn += 1
            if turn == X:
                find_fraction = True
                result = f'{i+1}/{k-i+1}'
                break
    else:
        for i in range(0, k+1):
            turn += 1
            if turn == X:
                find_fraction = True
                result = f'{i+1}/{k-i+1}'
                break
    if find_fraction:
        break
    else:
        k += 1

print(result)
