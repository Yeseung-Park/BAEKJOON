# 이것도 어려웠어... 왜지...ㅠ

from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    real_docs = deque()
    for i in range(N):
        real_docs.append((docs[i], i))

    cnt = 0    # 몇 번 째 출력인지 세는 변수

    while real_docs:
        current = real_docs.popleft()
        print_later = False
        for doc in real_docs:
            if doc[0] > current[0]:    # 우선순위가 더 큰게 있다면
                real_docs.append(current)    # 맨 뒤로 append
                print_later = True
                break
        if not print_later:    # 우선순위가 더 큰 게 없다면
            cnt += 1
            if current[1] == M:
                print(cnt)
                break