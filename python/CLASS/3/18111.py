# 이건 접근 방법 조차도 감이 안 와서 GPT한테 힌트를 달라고 했다.
# 어차피 높이가 최대 256까지니까 가능한 높이를 모두 계산해보라고 하네.
# 이래서 완전 탐색이구나... 이런 식의 완전 탐색...
# 이걸 왜 생각을 못 했을까 분발해야겠다.
# 시간 초과가 났는데 그냥 이차원 배열로 받지 말고 일차원 배열로 받아야겠다.
import sys

N, M, B = map(int, input().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
grounds = [cell for row in data for cell in row]
result = 1e9    # 결과 시간
result_height = 0     # 그 때의 높이

for i in range(min(grounds), max(grounds)+1):
    # 가능한 모든 높이로 걸리는 시간을 측정하자.
    # 가능한 모든 높이는 현재 땅의 최소 높이와 최대 높이의 사이
    # 우선 해당 높이보다 높은 애들을 파내는 작업부터 먼저 하자.
    # 그 다음 채워넣는데 채워넣어야 하는 애들이 인벤토리에 있는 수보다 적을 경우에 불가능
    # 그 외에는 가능
    dig = 0  # 파내야 하는 양
    fill = 0  # 채워넣어야 하는 양
    for ground in grounds:
        if ground > i:
            dig += ground - i
        elif ground < i:
            fill += i - ground
    # 만약 채워넣어야 하는 양이 파내야 하는 양 + 기존 인벤토리에 있는 블록보다 많을 경우 불가능
    if fill > dig + B:
        pass
    else:
        temp = dig * 2 + fill * 1
        if temp < result:
            result = temp
            result_height = i
        elif temp == result:
            if i > result_height:
                result_height = i

print(result, result_height)