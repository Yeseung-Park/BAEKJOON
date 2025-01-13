n = int(input())
result = 0

for i in range(n-2):
    temp = (n-2-i) * (i+1)
    result += temp

print(result)
print(3)