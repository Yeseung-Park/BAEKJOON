from heapq import heappush, heappop

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    heappush(meetings, (end, start))

# 그리디?
# 항상 끝나는 시간이 제일 빠른 것을 선택하자
# 근데 중요한건 시작하는 시간은 가장 최근에 했던 회의의 끝나는 시간 이상이어야 한다.
# 끝나는 시간을 기준으로 최소힙을 생각해보자

end = 0
result = 0

while meetings:
    meeting = heappop(meetings)
    if meeting[1] >= end:
        result += 1
        end = meeting[0]

print(result)