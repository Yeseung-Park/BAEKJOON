angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angle_list = [angle1, angle2, angle3]
angle_set = {angle1, angle2, angle3}

if sum(angle_list) == 180:
    if len(angle_set) == 1:
        print('Equilateral')
    elif len(angle_set) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')