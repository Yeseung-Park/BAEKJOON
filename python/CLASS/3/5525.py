# 이것도 GPT가 알려줬다...

N = int(input())    # O의 개수
# 찾아야하는 형태를 나타낸다 N이

M = int(input())    # 문자열의 개수
S = input()    # 문자열

# N은 결국 연속된 IOI의 개수를 의미하므로 이를 알아보는데에 집중한다.
# 찾아야하는 문자열 형태를 계속 비교하는 건 시간이 오래 걸린다.
result = 0
count = 0    # 연속된 IOI의 개수

i = 0    # 시작점
while i < M-1:    # 시작점이 끝에 다다를 때까지
    if S[i:i+3] == 'IOI':    # IOI 패턴이 등장했으면
        count += 1
        if count >= N:    # 우리가 필요로 하는만큼의 IOI 패턴이 등장했으면
            result += 1    # 결과에 하나 추가
        i += 2    # IOI 패턴은 두 칸씩 이동
    else:    # 패턴이 등장하지 않았다면
        count = 0    # 연속된게 초기화 되는 것이고
        i += 1    # 다음으로 넘어가서 확인

print(result)
