N = int(input())
numbers = list(map(int, input().split()))

result = 0

for number in numbers:
    if number == 1:
        continue
    is_disjoint = True
    for i in range(2, number):
        if number % i == 0:    # 약수가 있으면
            is_disjoint = False
            break
    if is_disjoint:
        result += 1

print(result)