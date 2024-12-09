# 이것도 지피티의 도움을 조금 받았기 때문에...
# 꼭 다시 풀어볼 것...

K, N = map(int, input().split())

# 제일 작은 랜선의 길이를 기준으로 생각해보자.
# 매번 가운데 값을 기준으로 생각해서 부족하면 더 작게, 충분하면 더 크게 자르는 걸로

lines = [0]*K
for i in range(K):
    lines[i] = int(input())

max_line = max(lines)

start = 1
end = max_line

result = 0

while start <= end:
    middle = (start + end) // 2
    total = 0    # 총 랜선의 개수
    for line in lines:
        total += line // middle
    if total < N:    # 랜선의 개수가 부족할 경우
        # 더 작게 잘라야 하는 것
        end = middle - 1
    elif total >= N:    # 랜선의 개수가 더 많을 경우
        # 더 크게 잘라야 하는 것
        result = middle
        start = middle + 1


print(result)