M = int(input())
N = int(input())

array = []

for number in range(M, N+1):
    if number == 1:
        continue
    is_disjoint = True
    for i in range(2, number):
        if number % i == 0:    # 약수일 경우
            is_disjoint = False
            break
    if is_disjoint:
        array.append(number)

if not array:
    print(-1)
else:
    print(sum(array))
    print(array[0])