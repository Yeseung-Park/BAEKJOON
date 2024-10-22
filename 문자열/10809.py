string = input()

result = [-1]*26    # 24개의 알파벳의 존재 유무를 나타내기 위한 리스트

for i in range(len(string)):
    if result[ord(string[i])-97] == -1:    # 한 번도 등장한 적이 없다면
        result[ord(string[i])-97] = i
    else:
        pass

print(*result)