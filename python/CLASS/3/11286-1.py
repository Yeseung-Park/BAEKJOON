import sys

N = int(input())    # 힙에 넣으려는 총 숫자의 개수

h = [0]*(N+1)    # 힙으로 인덱스 번호와 순서를 맞추기 위해 N+1
last = 0    # 아마 현재 위치를 나타내는 것 아닐까?
# 힙의 삽입은 항상 맨 뒤에서만 일어나기 때문에 last는 그 맨 뒤 자리를 의미한다.

def insert(n):
    global last
    last += 1
    h[last] = n    # 우선 맨 끝에 넣기
    c = last
    p = c//2    # 부모 노드
    while p >= 1:
        if abs(h[p]) > abs(h[c]) or (abs(h[p]) == abs(h[c]) and h[p] > h[c]):
            h[p], h[c] = h[c], h[p]
            c = p
            p = c//2
        else:
            break

def delete():
    global last
    if last == 0:
        return 0
    temp = h[1]    # 삭제는 항상 최상단에서 된다. temp는 최상단에 있었던 애를 반환하기 위해 저장해놓는 변수
    h[1] = h[last]    # 가장 마지막 노드를 최상단 자리에 갖다 넣고 조정
    last -= 1    # 가장 마지막 노드를 최상단에 갖다 놓았으니 last는 1 감소
    p = 1
    c = p*2    # 루트 노드를 자식과 비교하면서 재정렬
    while c <= last:    # 자식 노드가 있으면
        if c+1 <= last and abs(h[c]) > abs(h[c+1]):    # 오른쪽 자식이 더 작다면 얘를 위로 올려야 하므로 얘를 주시
            c += 1
        elif c+1 <= last and abs(h[c]) == abs(h[c+1]):
            if h[c] > h[c+1]:
                c += 1
        if abs(h[p]) > abs(h[c]):    # 부모의 절댓값이 더 크면
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        elif abs(h[p]) == abs(h[c]):
            if h[p] > h[c]:
                h[p], h[c] = h[c], h[p]
                p = c
                c = p*2
            else:
                break
        else:
            break
    return temp

for _ in range(N):
    t = int(sys.stdin.readline())
    if t != 0:
        insert(t)
    else:
        print(delete())
