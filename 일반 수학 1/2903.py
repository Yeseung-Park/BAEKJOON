# N번 거친 후 만들어진 정사각형의 개수를 X라고 하면
# (X^0.5+1)^2 개의 점이 있는 것

N = int(input())

squares = 4**N
result = int((squares**0.5+1)**2)

print(result)