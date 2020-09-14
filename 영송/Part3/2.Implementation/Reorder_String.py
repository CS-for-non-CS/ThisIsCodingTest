strings = list(input())
N = len(strings)
# 숫자랑 문자 구분하기 위한 기준점, 영문자는 많으니깐...
num_list = ['0','1','2','3','4','5','6','7','8','9']
# 숫자를 꺼내서 합치기 위한 매개변수
total = 0
# 문자를 꺼내서 넣기 위한 배열
ans = []
# 숫자 검사를 먼저 한 후 ord를 이용하여 곧바로 total에 합 계산
# 숫자가 아닌 것은 ans에 append
for i in range(N):
    if strings[i] in num_list:
        total += ord(strings[i]) - ord('0')
    else:
        ans.append(strings[i])
# 버블 정렬을 사용한 정렬
# ord 기능을 이용핳여 알파벳 끼리의 대소 비교 후 오름차순 정렬
for i in range(len(ans)-1):
    for j in range(i+1,len(ans)):
        if ord(ans[i]) >= ord(ans[j]):
            ans[i], ans[j] = ans[j], ans[i]
# 누적된 계산 값을 str 자료형 변환 후 append
ans.append(str(total))          ### 숫자가 나왔는지 안 나왔는지 체크해야함!!!!!
# 결과값 ''.jon 을 사용하여 print
print(''.join(ans))

