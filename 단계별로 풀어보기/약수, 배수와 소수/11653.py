N = int(input())

# 굳이 소수를 구할 필요 없이 2부터 시작해서 계속 나누다가 하나씩 늘려가면 되는구나
# 어차피 2의 배수들은 이미 다 나눠졌을테니...
# 이런걸 생각 못하다니 멍청이인가

num = 2

while N > 1:
    if N % num == 0:
        N //= num
        print(num)
    else:
        num += 1