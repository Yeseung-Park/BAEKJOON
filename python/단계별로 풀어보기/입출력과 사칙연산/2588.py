a = int(input())
b = int(input())

b_1 = b % 10
b_10 = ((b - b_1) % 100) // 10
b_100 = (b - (b_1 + b_10)) // 100

print(a*b_1)
print(a*b_10)
print(a*b_100)
print(a*b)