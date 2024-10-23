while True:
    n = int(input())
    if n == -1:
        break
    else:
        sum = 0
        array = []
        for i in range(1, n//2+1):
            if n % i == 0:
                sum += i
                array.append(i)
        if sum == n:
            real_array = map(str, array)
            string = ' + '.join(real_array)
            print(f'{n} = {string}')
        else:
            print(f'{n} is NOT perfect.')