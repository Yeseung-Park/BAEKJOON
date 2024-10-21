N = int(input())

numbers = list(map(int, input().split()))

find_num = int(input())

cnt = 0

for num in numbers:
    if num == find_num:
        cnt += 1

print(cnt)