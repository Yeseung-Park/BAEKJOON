while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    else:
        result = A+B
        print(result)