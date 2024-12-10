import sys

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


print(arr)