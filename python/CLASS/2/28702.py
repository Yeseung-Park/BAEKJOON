s1 = input()
s2 = input()
s3 = input()

if s3.isdecimal():    # 마지막에 나열한 것이 숫자이면
    result = int(s3) + 1
    if result % 3 == 0 and result % 5 == 0:    # 3의 배수이면서 5의 배수이면
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)
elif s2.isdecimal():
    result = int(s2) + 2
    if result % 3 == 0 and result % 5 == 0:    # 3의 배수이면서 5의 배수이면
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)
else:
    result = int(s1) + 3
    if result % 3 == 0 and result % 5 == 0:    # 3의 배수이면서 5의 배수이면
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)

# 근데 이런 하드코딩을 노린 건 아닐 것 같은데;;