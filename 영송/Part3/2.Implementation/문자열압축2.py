#s1 = "aabbaccc" # result = 7
#s2 = "abcabcdede" # result = 8
s1 = 'xababcdcdababcdcd'
N = len(s1)
min_val = N
for i in range(1,N//2+1):
    cnt = 0
    flag = 0
    total = 0
    print('p:',i)
    for j in range(N-i+1):
        pattern = s1[j:j+i]
        print('pattern:',pattern)
        for k in range(j+i,N-i+1,i):
            if pattern == s1[k:k+i]:
                flag = 1
                cnt += 1
                print('pattern correct',cnt)
            else:
                pattern = s1[k:k+i]
                print('new pattern',pattern)
                total += cnt*i - flag
                print('total',total,cnt,flag)
                flag = 0
                cnt = 0
        if cnt !=0:
            print(cnt,flag)
            total += cnt*i - flag
            cnt = 0
        print('total:',total)
        if N-total < min_val:
            min_val = N-total
        total = 0
print(min_val)