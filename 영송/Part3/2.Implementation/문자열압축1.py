def solution(s):
    N = len(s)
    answer = N
    for i in range(1,N//2+1):
        cnt = 0
        flag = 0
        total = 0
        for j in range(N-i+1):
            pattern = s[j:j+i]
            for k in range(j+i,N-i+1,i):
                if pattern == s[k:k+i]:
                    flag = 1
                    cnt += 1
                else:
                    pattern = s[k:k+i]
                    total += cnt*i - flag
                    flag = 0
                    cnt = 0
            total += cnt*i - flag
            cnt = 0
            if N-total < answer:
                answer = N-total
            total = 0
    return answer

s = 'xababcdcdababcdcd'
print(solution(s))