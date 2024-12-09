# 제일 왼쪽에 있는 점의 x좌표 -> 왼쪽 세로 경계
# 제일 오른쪽에 있는 점의 x 좌표 -> 오른쪽 세로 경계
# 제일 위쪽에 있는 점의 y 좌표 -> 위쪽 가로 경계
# 제일 아래쪽에 있는 점의 y 좌표 -> 아래쪽 가로 경계

N = int(input())

x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

left_boundary = min(x_list)
right_boundary = max(x_list)
up_boundary = max(y_list)
down_boundary = min(y_list)

width = right_boundary - left_boundary
height = up_boundary - down_boundary

print(width*height)