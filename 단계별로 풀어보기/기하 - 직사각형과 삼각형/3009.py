x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_list = [x1, x2, x3]
y_list = [y1, y2, y3]
x_set = {x1, x2, x3}
y_set = {y1, y2, y3}

for x in x_set:
    if x_list.count(x) == 1:
        x4 = x
        break

for y in y_set:
    if y_list.count(y) == 1:
        y4 = y
        break

print(x4, y4)