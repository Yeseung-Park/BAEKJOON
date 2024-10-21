numbers = list(map(int, input().split()))

N = len(set(numbers))

if N == 3:    # 모두 다른 눈
    result = max(numbers) * 100
elif N == 2:    # 같은 눈이 2개
    for i in range(2):
        find_result = False
        for j in range(1, 3):
            if numbers[i] == numbers[j]:
                result = 1000 + numbers[i] * 100
                find_result = True
                break
        if find_result:
            break
else:
    result = 10000 + numbers[0] * 1000

print(result)