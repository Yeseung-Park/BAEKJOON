N = int(input())

i = 1

if N == 1:
    print(1)
else:
    N -= 1
    while N > 6*i:
        N -= 6*i
        i += 1
    print(i+1)