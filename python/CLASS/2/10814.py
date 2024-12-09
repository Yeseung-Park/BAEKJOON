N = int(input())    # 온라인 저지 회원의 수

members = []

for i in range(N):
    x, y = input().split()
    age = int(x)
    members.append((age, y, i))
    # (나이, 이름, 가입한 순서)

members.sort(key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])

# 뭔가 시간이 오래 걸리긴 했는데 맞았으니까...