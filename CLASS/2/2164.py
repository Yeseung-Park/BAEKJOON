from collections import deque

N = int(input())
queue = deque()

for i in range(1, N+1):
    queue.append(i)

cnt = 0

while len(queue) > 1:
    if cnt % 2 == 0:    # 짝수 번째이면
        temp = queue.popleft()
        cnt += 1
    else:    # 홀수 번째이면
        temp = queue.popleft()
        queue.append(temp)
        cnt += 1

result = queue.popleft()

print(result)