T = int(input())

for tc in range(T):
    # 이것도 스택을 이용하자.
    strings = input()
    stack = []
    is_right = True
    for string in strings:
        if string == '(':
            stack.append(string)
        else:
            if stack:
                stack.pop()
            else:
                is_right = False
    if stack == [] and is_right:
        print('YES')
    else:
        print('NO')