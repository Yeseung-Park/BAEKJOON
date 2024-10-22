grade_score = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

sum_of_credit_grade = 0
sum_of_credit = 0

for _ in range(20):
    subject, credit, grade = input().split()
    real_credit = float(credit)
    if grade == 'P':
        pass
    else:
        sum_of_credit_grade += real_credit * grade_score[grade]
        sum_of_credit += real_credit

result = sum_of_credit_grade / sum_of_credit

print(result)