while True:
    num = int(input())
    if num == 0:
        break
    else:
        str_num = str(num)
        if str_num == str_num[::-1]:
            print('yes')
        else:
            print('no')