T = int(input())

Q = 25
D = 10
N = 5
P = 1

for tc in range(1, T+1):
    C = int(input())
    quarter = C // Q
    C %= Q
    dime = C // D
    C %= D
    nickel = C // N
    C %= N
    penny = C // P
    print(quarter, dime, nickel, penny)