numbers = list(map(int, input().split()))

numbers = list(map(lambda x: x**2, numbers))

temp = sum(numbers)

result = temp % 10

print(result)