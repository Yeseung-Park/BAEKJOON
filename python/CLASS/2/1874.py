import sys

n = int(sys.stdin.readline())
numbers = [0]*n

for i in range(n):
    numbers[i] = int(sys.stdin.readline())

i = 0
j = 1

stack = []
result = []

possible = True

while i < n:
    current = numbers[i]
    if not stack:
        stack.append(j)
        result.append('+')
        j += 1
    else:
        if stack[-1] != current:
            if j <= n:
                stack.append(j)
                result.append('+')
                j += 1
            else:
                possible = False
                print('NO')
                break
        else:
            stack.pop()
            result.append('-')
            i += 1

if possible:
    for i in range(len(result)):
        print(result[i])