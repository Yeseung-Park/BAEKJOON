# 이건 진짜 모르겠어서 지피티 도움을 많이 받았다...
# 난 쓰레기야...

N, K = map(int, input().split())

people = [0]*N
result = []

for i in range(1, N+1):
    people[i-1] = i

current_idx = 0

while people:
    index = (current_idx + K-1) % len(people)
    person = people.pop(index)
    result.append(str(person))
    current_idx = index

result_str = ', '.join(result)
print('<' + result_str + '>')