T = int(input())

for tc in range(1, T+1):
    string = input()
    s1, s2 = string[0], string[-1]
    result = s1 + s2
    print(result)