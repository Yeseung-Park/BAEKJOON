N = int(input())

people = list(map(int, input().split()))

# 돈을 뽑는데 걸리는 시간이 짧은 사람부터 돈을 뽑자!

# 우선 오름차순으로 정리하자!

people.sort()

time = []

for person in people:
    if not time:
        time.append(person)
    else:
        temp = time[-1]
        time.append(temp+person)

print(sum(time))