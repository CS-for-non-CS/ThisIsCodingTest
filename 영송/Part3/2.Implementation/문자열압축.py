# https://programmers.co.kr/learn/courses/30/lessons/60057

#s = "aabbaccc" # result = 7
#s = "abcabcdede" # result = 8
#s = 'xababcdcdababcdcd' # result = 17
#s = 'abcabcabcabcdededededede' #result = 14
def solution(s):
    N = len(s)
    answer = N

    for i in range(1,N//2+1):
        cnt = 1
        total = 0
        pattern = s[:i]

        # cnt 가 두 자리수이면 flag가 2가 될 수도 있음
        for k in range(i,N,i):
            if pattern == s[k:k+i]:
                cnt += 1
            else:
                pattern = s[k:k+i]
                total += cnt*i - (cnt//10+1)
                cnt = 0

        if cnt !=0:
            total += cnt*i - (cnt//10+1)
            cnt = 0

        if N-total < answer:
            answer = N-total
        total = 0

    return answer

print(solution(s))