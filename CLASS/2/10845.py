from collections import deque
import sys

N = int(input())    # 명령의 수
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        num = command.split()
        queue.append(num[1])
    elif command == 'pop':
        if queue:
            temp = queue.popleft()
            print(temp)
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)