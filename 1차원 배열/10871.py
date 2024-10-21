N, X = map(int, input().split())

numbers = list(map(int, input().split()))

result = []

for number in numbers:
    if number < X:
        result.append(number)

print(*result)