H, M = map(int, input().split())

if M-45 < 0:
    new_H = H-1
    new_M = 60+(M-45)
    if new_H < 0:
        new_H = 24+new_H
    print(new_H, new_M)
else:
    new_M = M-45
    print(H, new_M)

# if new_H < 0:
#     new_H = 24+new_H