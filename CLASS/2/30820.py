N = int(input())    # 참가자의 수
sizes = list(map(int, input().split()))    # 사이즈별 수량
# [S, M, L, XL, XXL, XXXL]
T, P = map(int, input().split())    # T: 티셔츠 묶음 수, P: 펜 묶음 수

shirts_sum = 0

for size in sizes:
    if size % T == 0:
        shirts_sum += size // T
    else:
        shirts_sum += size // T + 1

pen_group = N // P
pen_indiv = N % P

print(shirts_sum)
print(pen_group, pen_indiv)