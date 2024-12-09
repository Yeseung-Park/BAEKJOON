K = int(input())

# 이것도 가장 최근에 쓴 수를 지우는거니까 스택이다.

stack = []

for _ in range(K):
    num = int(input())
    if num == 0:
        if not stack:    # 스택이 비어있을 경우에는
            pass    # 넘어가기
        else:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))