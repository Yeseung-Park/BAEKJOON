N = int(input())    # 상근이가 가지고 있는 숫자카드의 개수
numbers = list(map(int, input().split()))

numbers_dict = {}

M = int(input())    # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수
find_numbers = list(map(int, input().split()))

result = [0]*M

# 딕셔너리로 저장하면 될 것 같긴 한데
for number in numbers:
    if number in numbers_dict.keys():
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

for i in range(M):
    find_number = find_numbers[i]
    if find_number in numbers_dict.keys():
        result[i] = numbers_dict[find_number]
    else:
        result[i] = 0

print(*result)
