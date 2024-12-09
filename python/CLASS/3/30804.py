import sys
sys.setrecursionlimit(200000)

N = int(input())    # 과일의 개수

fruits = list((map(int, input().split())))

maximum = 0

def remove(start, end):
    # 먼저 앞에서 빼주고 뒤에서 빼주면 될 것 같은디...
    # deque을 이용할까
    # 그런데 시간이 너무 오래 걸리니까 인덱스로 생각해야한다.
    # start는 시작 인덱스 end는 마지막 인덱스
    global maximum

    if end - start < 2:    # 여기서부터는 더 이상 찾을 필요가 없다.
        maximum = max(end-start, maximum)
        return

    if len(set(fruits[start:end])) <= 2:
        if len(fruits[start:end]) > maximum:
            maximum = len(fruits[start:end])
        return

    remove(start+1, end)    # 앞에서 제거
    remove(start, end-1)    # 뒤에서 제거

remove(0, N)

print(maximum)