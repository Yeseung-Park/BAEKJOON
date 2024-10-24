import sys

N = int(input())

numbers = []

for _ in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

for num in numbers:
    print(num)