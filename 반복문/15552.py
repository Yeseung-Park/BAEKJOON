import sys

T = int(sys.stdin.readline().rstrip())

for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)