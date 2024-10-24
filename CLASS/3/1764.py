import sys

N, M = map(int, input().split())
# N: 듣도 못한 사람, M: 보도 못한 사람

not_seen = set()
not_heard = set()

for _ in range(N):
    person = sys.stdin.readline().strip()
    not_seen.add(person)

for _ in range(M):
    person = sys.stdin.readline().strip()
    not_heard.add(person)

not_seen_heard = not_seen.intersection(not_heard)

not_seen_heard_list = sorted(list(not_seen_heard))

print(len(not_seen_heard_list))

for person in not_seen_heard_list:
    print(person)