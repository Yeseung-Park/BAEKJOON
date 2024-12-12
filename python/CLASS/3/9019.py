# D: 2n%10000을 레지스터에 저장
# S: n-1을 레지스터에 저장 (n이 0이라면 9999를 레지스터에 저장)
# L: n의 각 자리수를 왼편으로 회전
# R: n의 각 자리수를 오른편으로 회전
# L과 R은 원형큐를 생각하면 될 것 같다.

# BFS?

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
