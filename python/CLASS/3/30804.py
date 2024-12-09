import sys
sys.setrecursionlimit(200000)

N = int(input())    # 과일의 개수

fruits = list((map(int, input().split())))

maximum = 0

count = {}
# 과일의 종류랑 개수를 담을 딕셔너리

# 슬라이딩 윈도우 기법을 사용하라.
# 슬라이딩 윈도우 기법
# 시작과 끝 포인터를 조절하여 두 종류의 과일만 포함된 연속 구간의 길이를 계산
# 시작 지점은 0에서 시작하고 끝 지점은 점점 키운다.

start = 0

for end in range(N):
    count[fruits[end]] = count.get(fruits[end], 0) + 1

    while len(count) > 2:    # 과일의 개수가 두 종류 이상이면 시작점을 바꿔서 범위를 좁힌다.
        count[fruits[start]] -= 1
        if count[fruits[start]] == 0:    # 0이 됐으면 과일 제거
            del count[fruits[start]]
        start += 1    # 범위 좁히기

    # 여기까지 왔으면 과일의 개수가 두 종류 이상이 아니라는 것이며 이때 과일의 개수를 체크해야 한다.
    maximum = max(maximum, end - start + 1)

# 이걸 끝 점이 과일 배열의 끝까지 될 때까지 반복하면 최댓값을 구할 수 있다.
# 솔직히 GPT가 알려준거라 나중에 다시 풀어봐야 할 듯

print(maximum)