A, B, V = map(int, input().split())

real = A - B    # 실제로 하루에 올라가는 높이

# 마지막 날에는 미끄러지지 않으므로 실제로 날 수를 계산하기 위해 올라가야 하는 높이는
real_height = V - A
# 이게 진짜 중요하다... 이렇게 계산하면 편한데...

if real_height % real != 0:    # 올림
    day = real_height // real + 1
else:
    day = real_height // real

print(day+1)