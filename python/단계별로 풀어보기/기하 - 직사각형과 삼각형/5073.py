while True:
    s1, s2, s3 = map(int, input().split())
    if s1 == 0 and s2 == 0 and s3 == 0:
        break
    else:
        s_list = [s1, s2, s3]
        s_set = {s1, s2, s3}
        max_side = max(s_list)
        max_side_idx = s_list.index(max_side)
        another_sum = 0
        for i in range(3):
            if i == max_side_idx:
                pass
            else:
                another_sum += s_list[i]
        if max_side >= another_sum:
            print('Invalid')
        else:
            if len(s_set) == 1:
                print('Equilateral')
            elif len(s_set) == 2:
                print('Isosceles')
            else:
                print('Scalene')