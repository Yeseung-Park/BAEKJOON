# 뭔가 큐를 쓰면 될 것 같기도 하고 아닐 것 같기도 하고

from collections import deque

N = int(input())    # 전체 종이의 한 변의 길이

paper = [list(map(int, input().split())) for _ in range(N)]

squares = deque()
squares.append((0, 0, N))
# 체크해야하는 정사각형의 왼쪽 위 지점을 square에 담기
# (행, 열, 정사각형의 크기)

white = 0
blue = 0    # 하얀색, 파란색 색종이의 개수

while squares:    # 체크해야하는 정사각형이 다 없어질 때까지
    ti, tj, length = squares.popleft()
    if paper[ti][tj] == 1:    # 왼쪽 끝이 파란색일 경우
        # 모든 애들이 파란색이어야 만족
        is_all_blue = True
        for i in range(ti, ti+length):
            for j in range(tj, tj+length):    # 정사각형 안의 모든 원소 탐색
                if paper[i][j] == 0:    # 하얀색이 있으면
                    is_all_blue = False
                    break
            if is_all_blue == False:
                break
        if is_all_blue:
            blue += 1
        else:
            new_length = length // 2
            squares.append((ti, tj, new_length))
            squares.append((ti, tj+new_length, new_length))
            squares.append((ti+new_length, tj, new_length))
            squares.append((ti+new_length, tj+new_length, new_length))
    else:    # 왼쪽 끝이 하얀색일 경우
        # 모든 애들이 하얀색이어야 만족
        is_all_white = True
        for i in range(ti, ti+length):
            for j in range(tj, tj+length):    # 정사각형 안의 모든 원소 탐색
                if paper[i][j] == 1:    # 파란색이 있으면
                    is_all_white = False
                    break
            if is_all_white == False:
                break
        if is_all_white:
            white += 1
        else:
            new_length = length // 2
            squares.append((ti, tj, new_length))
            squares.append((ti, tj+new_length, new_length))
            squares.append((ti+new_length, tj, new_length))
            squares.append((ti+new_length, tj+new_length, new_length))

print(white)
print(blue)
