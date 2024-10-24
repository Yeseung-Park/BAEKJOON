N = int(input())    # 기준이 되는 정수의 개수
numbers1 = list(map(int, input().split()))    # 기준이 되는 정수
M = int(input())
numbers2 = list(map(int, input().split()))    # 비교할 정수

numbers1.sort()

def binary_search(key, list):
    start, end = 0, len(list)-1
    while start <= end:
        middle = (start + end) // 2
        if list[middle] == key:
            return 1
        elif list[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

for number2 in numbers2:
    result = binary_search(number2, numbers1)
    print(result)