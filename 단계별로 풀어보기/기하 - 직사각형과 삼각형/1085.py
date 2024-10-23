x, y, w, h = map(int, input().split())

array = [h-y, y, w-x, x]

print(min(array))