scale = list(map(int, input().split()))

asc_scale = sorted(scale)
desc_scale = sorted(scale, reverse=True)

if scale == asc_scale:
    print('ascending')
elif scale == desc_scale:
    print('descending')
else:
    print('mixed')