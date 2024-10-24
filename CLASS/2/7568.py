N = int(input())

result = [0] * N

# 그냥 모든 애들을 냅다 하나씩 비교해볼까요

people = []

for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(N):
    temp = 0    # 나보다 덩치가 큰 사람 수
    weight1, height1 = people[i][0], people[i][1]
    for j in range(N):
        if i == j:
            continue
        weight2, height2 = people[j][0], people[j][1]
        if weight1 < weight2 and height1 < height2:    # 키와 몸무게 둘 다 본인보다 크면
            # 본인보다 덩치가 큰 사람이라는 것
            temp += 1
    result[i] = temp+1

print(*result)

# 그냥 복잡하게 생각하지 말고 하나하나 보면서 자기보다 덩치가 큰 사람만 고려하는 것이 포인트!
# 왜 이렇게 복잡하게 생각했는지 모르겠다...
# 시간이 그렇게 오래 걸리는 것도 아닌데...