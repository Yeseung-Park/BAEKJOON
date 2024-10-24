N = int(input())

start = 666
cnt = 0

while True:
    start_str = str(start)
    if '666' in start_str:
        cnt += 1
        if cnt == N:
            print(start_str)
            break
    start += 1