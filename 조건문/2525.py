A, B = map(int, input().split())
C = int(input())

if B+C >= 60:    # 60분을 넘어가면
    new_B = (B+C) % 60
    new_A = A + (B+C) // 60
    if new_A >= 24:
        new_A -= 24
    print(new_A, new_B)
else:
    B = B+C
    print(A, B)