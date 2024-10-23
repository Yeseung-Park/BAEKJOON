N = int(input())

# 생성자는 N-9*자릿수 이상의 숫자다.
str_N = str(N)
i = max(1, N - 9*(len(str_N)))
# i는 음수가 되면 안 된다.
find = False

# 종료 포인트 잘 설정해주자!
while i < N:
    str_i = str(i)
    total = i
    for s in str_i:
        total += int(s)
    if total == N:
        result = i
        find = True
        break
    else:
        i += 1

if not find:
    print(0)
else:
    print(result)