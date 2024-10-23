N, M = map(int, input().split())
# N: 카드의 개수, M: 기준이 되는 합
cards = list(map(int, input().split()))

# 카드를 정렬한 다음
# 가장 큰 경우부터 하나씩 하면 될 것 같은데

cards = sorted(cards, reverse=True)
# 내림차순으로 카드 정렬

find_blackjack = set()

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                find_blackjack.add(total)

print(max(find_blackjack))