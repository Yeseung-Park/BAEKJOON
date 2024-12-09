import sys

N = int(input())    # 명령의 수

stack = [0]*N
top = -1

for _ in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        num = command.split()
        top += 1
        stack[top] = num[-1]
    elif command == 'pop':
        if top >= 0:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif command == 'size':
        print(top+1)
    elif command == 'empty':
        if top >= 0:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if top >= 0:
            print(stack[top])
        else:
            print(-1)