N = int(input())

result = 1e9

for x in range(2000):    # 3kg 봉지의 개수
    for y in range(1001):    # 5kg 봉지의 개수
        temp = x*3 + y*5
        if temp == N:
            result = min(result, x+y)

if result == 1e9:
    print(-1)
else:
    print(result)