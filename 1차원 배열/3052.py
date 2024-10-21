result = set()

for _ in range(10):
    num = int(input())
    temp = num % 42
    result.add(temp)

print(len(result))