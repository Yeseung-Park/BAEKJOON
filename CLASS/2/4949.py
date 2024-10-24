# 스택을 이용해야 할 것 같다.

while True:
    text = input()
    if text == '.':
        break
    else:
        stack = []    # 여는 괄호 담는 스택
        is_right = True
        for string in text:
            if string == '(' or string == '[':
                stack.append(string)
            elif string == ')':
                if stack:
                    temp = stack.pop()
                    if temp != '(':
                        is_right = False
                        break
                else:
                    is_right = False
                    break
            elif string == ']':
                if stack:
                    temp = stack.pop()
                    if temp != '[':
                        is_right = False
                        break
                else:
                    is_right = False
                    break

        if stack == [] and is_right:
            # 둘 다 짝을 찾아서 잘 갔으면
            print('yes')
        else:
            print('no')
