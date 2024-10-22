str1, str2 = input().split()

new_int1 = int(str1[::-1])
new_int2 = int(str2[::-1])

if new_int1 > new_int2:
    print(new_int1)
else:
    print(new_int2)