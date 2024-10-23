T = int(input())

for tc in range(1, T+1):
    r, S = input().split()
    R = int(r)
    result = ''
    for s in S:
        result += s*R

    print(result)