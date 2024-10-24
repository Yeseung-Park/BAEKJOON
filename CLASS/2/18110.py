import sys

n = int(sys.stdin.readline())    # 난이도 의견의 개수

levels = [0]*n

for i in range(n):
    levels[i] = int(sys.stdin.readline())

levels.sort()    # 우선 오름차순으로 정렬

# 15%가 몇 명에 해당하는지 구하기
exclude_people = int(n*0.15 + 0.5)

if  n <= 2*exclude_people:
    print(0)
else:
    real_levels = levels[exclude_people:n-exclude_people]
    mean = int(sum(real_levels)/(n-2*exclude_people) + 0.5)
    print(mean)

# 반올림을 직접 구현하는 방법
# 반올림 하려는 수에 0.5를 더하고 내린다.
# 내림하는 방법은 그냥 int로 형변환하면 된다.