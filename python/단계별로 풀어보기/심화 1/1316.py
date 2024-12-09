N = int(input())
result = 0

for _ in range(N):
    string = input()
    string_alpha = set(string)
    is_group = True
    for alpha in string_alpha:
        index = []
        for i in range(len(string)):
            if string[i] == alpha:
                index.append(i)
        for i in range(0, len(index)-2+1):
            if index[i+1]-index[i] > 1:    # 그룹 단어가 아니다.
                is_group = False
                break
        if not is_group:
            break
    if is_group:
        result += 1

print(result)