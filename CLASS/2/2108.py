import sys

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 평균
total = sum(numbers)
temp = total / N
if temp >= 0:
    mean = int(temp + 0.5)
elif temp < 0:
    mean = int(temp - 0.5)

print(mean)

# 중앙값
numbers.sort()
middle = numbers[len(numbers) // 2]
print(middle)

# 최빈값
num_count_dict = {}
for num in numbers:
    if num in num_count_dict.keys():
        num_count_dict[num] += 1
    else:
        num_count_dict[num] = 1

max_count = max(num_count_dict.items(), key=lambda x: x[1])
max_list = []

for key, value in num_count_dict.items():
    if value == max_count:
        max_list.append(key)

if len(max_list) == 1:
    print(max_list[0])
else:
    print(max_list[1])

# 범위
range = numbers[-1] - numbers[0]
print(range)