while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if B % A == 0:    # A가 B의 약수일 경우
            print('factor')
        elif A % B == 0:    # A가 B의 배수일 경우
            print('multiple')
        else:
            print('neither')
