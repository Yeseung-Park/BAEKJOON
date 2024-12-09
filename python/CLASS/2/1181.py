N = int(input())    # 단어의 개수

words = set()

for _ in range(N):
    words.add(input())

words_list = list(words)

words_list.sort(key=lambda x: [len(x), x])

for word in words_list:
    print(word)