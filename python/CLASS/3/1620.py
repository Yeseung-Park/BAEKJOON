import sys

N, M = map(int, input().split())

num_pokemons = {}    # 번호: 이름
pokemons_num = {}    # 이름: 번호

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    num_pokemons[i] = name
    pokemons_num[name] = i

for _ in range(M):
    quiz = sys.stdin.readline().strip()
    if quiz.isdecimal():    # 숫자로 들어온 문제일 경우
        # 해당 번호를 가진 포켓몬을 말해야 한다.
        print(num_pokemons[int(quiz)])
    else:    # 문자로 들어온 문제의 경우
        # 해당 포켓몬의 번호를 말해야 한다.
        print(pokemons_num[quiz])