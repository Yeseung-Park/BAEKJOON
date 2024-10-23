while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    else:
        side_list = [a, b, c]
        max_side = max(side_list)
        max_side_idx = side_list.index(max_side)
        another_sum = 0
        for i in range(3):
            if i == max_side_idx:
                pass
            else:
                another_sum += side_list[i]**2

        if another_sum == max_side**2:
            print('right')
        else:
            print('wrong')