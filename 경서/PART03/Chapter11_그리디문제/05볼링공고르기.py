'''
5 3
1 3 2 3 2
8 5
1 5 4 3 2 4 5 2
'''
N,M = map(int, input().split())
arr= list(map(int, input().split()))

result = 0
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] != arr[j]:
            result += 1
print(result)