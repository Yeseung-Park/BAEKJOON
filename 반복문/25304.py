X = int(input())    # 영수증에 적힌 총 금액
N = int(input())    # 영수증에 적힌 구매한 물건의 종류의 수
real_cost = 0
for _ in range(N):
    price, num = map(int, input().split())
    real_cost += price * num

if real_cost == X:
    print('Yes')
else:
    print('No')