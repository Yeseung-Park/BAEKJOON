numbers = list()

for _ in range(9):
    numbers.append(int(input()))

result_num = max(numbers)
result_index = numbers.index(result_num) + 1

print(result_num)
print(result_index)