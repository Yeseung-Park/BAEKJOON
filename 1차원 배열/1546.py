N = int(input())    # 시험 본 과목의 개수

scores = list(map(int, input().split()))    # 세준이의 현재 성적

max_score = max(scores)

new_score = [0]*N

for i in range(N):
    new_score[i] = scores[i]/max_score*100

sum_score = sum(new_score)

result = sum_score/N

print(result)