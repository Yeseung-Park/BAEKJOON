alphabet = list(input())

length = len(alphabet)
result = 0

croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatia_alpha:
    for i in range(0, len(alphabet)-len(alpha)+1):
        if ''.join(alphabet[i:i+len(alpha)]) == alpha:
            result += 1
            alphabet[i:i+len(alpha)] = ['0']*len(alpha)

for alpha in alphabet:
    if alpha.isalpha():
        result += 1

print(result)