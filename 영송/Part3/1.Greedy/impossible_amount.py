N = int(input())
numbers = list(map(int,input().split()))
ans = numbers
# 테스트 케이스 overfitting
# max_val = max(numbers)

# 가지 치기가 필요함, 아니면 10개 부터 못풀어냄;;
def subsetsum(n,k,currsum):
    global max_val
    global ans
    #if currsum > max_val:
        #return
    if n==k:
        if currsum not in ans:
            ans.append(currsum)
        return
    else:
        subsetsum(n,k+1,currsum + numbers[k])
        subsetsum(n,k+1,currsum)

subsetsum(N,0,0)

max_val = max(ans)
for i in range(1,max_val):
    if i not in ans:
        break

print(i)