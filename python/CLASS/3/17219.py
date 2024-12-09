import sys

N, M = map(int, input().split())

site_password = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    site_password[site] = password

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(site_password[site])