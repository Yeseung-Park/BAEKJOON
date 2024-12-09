T = int(input())

for tc in range(T):
    quizes = list(input())
    cumulative = 0
    result = 0
    for quiz in quizes:
        if quiz == 'X':
            cumulative = 0
        else:
            result += cumulative + 1
            cumulative += 1

    print(result)