T = int(input())

for tc in range(T):
    p = input()    # 수행할 함수
    n = int(input())    # 배열에 들어있는 수의 개수
    numbers_str = input()
    numbers_str = numbers_str.strip('[]')

    numbers = numbers_str.split(',')

    start, end = 0, n-1    # 배열의 시작과 끝을 가리키는 변수
    reverse = False
    error = False

    for func in p:
        if func == 'R':
            if reverse:    # 뒤집혀져 있는 상태라면
                start, end = end, start
                reverse = False
            else:
                start, end = end, start
                reverse = True
        else:    # 제일 앞에 있는 애 지우기
            if reverse:    # 뒤집혀져 있는 상태
                if start < end:    # 뒤집혀져 있는데 start < end라는 것은 비어있다는 것
                    error = True
                    print('error')
                    break
                else:
                    start -= 1
            else:
                if start > end:
                    error = True
                    print('error')
                    break
                else:
                    start += 1
    if not error:
        result = '['
        if reverse:
            if end-1 < 0:
                temp = ','.join(numbers[start::-1])
                result += temp
                result += ']'
                print(result)
            else:
                temp = ','.join(numbers[start:end-1:-1])
                result += temp
                result += ']'
                print(result)
        else:
            temp = ','.join(numbers[start:end+1])
            result += temp
            result += ']'
            print(result)