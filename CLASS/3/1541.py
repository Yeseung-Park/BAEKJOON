# -뒤에는 다 괄호를 만드는게 좋지 않을까...?
# 아니면 무조건 - 뒤에 있는 숫자부터 계산?

formula = input()

formula_list = formula.split('-')    # -를 기준으로 분해

for i in range(len(formula_list)):    # 각각에 대해서
    if formula_list[i].isdecimal():    # only 숫자일 경우
        formula_list[i] = int(formula_list[i])
        # 정수로 형변환해서 재할당
    else:    # 계산이 섞여있다면
        second_formula_list = formula_list[i].split('+')
        # 일단 + 로 다 나눠주고 숫자만 남겨서 더해줍시다
        temp = 0
        for num in second_formula_list:
            temp += int(num)
        formula_list[i] = temp
        # 계산해서 재할당

if formula[0] == '-':    # -로 시작하는 숫자였다면
    result = formula_list[0]*(-1)
    for i in range(1, len(formula_list)):
        result -= formula_list[i]
else:
    result = formula_list[0]
    for i in range(1, len(formula_list)):
        result -= formula_list[i]

print(result)
