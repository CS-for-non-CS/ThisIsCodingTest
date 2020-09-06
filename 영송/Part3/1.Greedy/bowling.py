N,M = map(int,input().split())
bowling = list(map(int,input().split()))
A = [0] * N
cnt = 0
def subset(n,k):
    global cnt
    if n==k:
        select = []
        if sum(A) == 2:
            for i in range(n):
                if A[i] == 1:
                    if len(select) !=0:
                        check = select.pop()
                        if bowling[i] != check:
                            cnt += 1
                    else:
                        select.append(bowling[i])
    else:
        A[k] = 1
        subset(n,k+1)
        A[k] = 0
        subset(n,k+1)

subset(N,0)
print(cnt)