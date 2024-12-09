def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

N = int(input())

num = fact(N)

str_num = str(num)

cnt = 0

for s in str_num[::-1]:
    if s == '0':
        cnt += 1
    else:
        break

print(cnt)