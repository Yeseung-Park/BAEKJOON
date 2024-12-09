A, B = map(int, input().split())

# A와 B를 소인수분해 한 값을 먼저 알아야겠다.

A_dict = {}
B_dict = {}

i, j = 2, 2

while A > 1:
    if A % i == 0:    # 나누어 떨어지면
        A //= i
        if i in A_dict.keys():
            A_dict[i] += 1
        else:
            A_dict[i] = 1
    else:
        i += 1

while B > 1:
    if B % j == 0:    # 나누어 떨어지면
        B //= j
        if j in B_dict.keys():
            B_dict[j] += 1
        else:
            B_dict[j] = 1
    else:
        j += 1

# 최대공약수부터 구하자
maximum = 1
for key, value in A_dict.items():
    if key in B_dict.keys():    # B에도 있는 소인수일 경우
        exp = min(value, B_dict[key])
        maximum *= key**exp

# 그 다음 최소공배수
minimum = 1
for key, value in A_dict.items():
    if key in B_dict.keys():
        exp = max(value, B_dict[key])
        minimum *= key**exp
    else:
        minimum *= key**value

for key, value in B_dict.items():
    if key not in A_dict.keys():
        minimum *= key**value

print(maximum)
print(minimum)