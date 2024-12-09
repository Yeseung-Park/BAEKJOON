N, K = map(int, input().split())

i = 1
cnt = 0

while True:
    if i > N:
        result = 0
        break
    if N % i == 0:
        cnt += 1
        if K == cnt:
            result = i
            break
    i += 1

print(result)