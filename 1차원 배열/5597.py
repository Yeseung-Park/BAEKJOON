students = [0] * 30

for _ in range(28):
    number = int(input())
    students[number-1] = number

for i in range(30):
    if students[i] == 0:
        print(i+1)