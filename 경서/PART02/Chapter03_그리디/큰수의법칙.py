'''
5 8 3
2 4 5 4 6
'''

N,M,K = map(int, input().split())
arr = list(map(int, input().split()))
result = []
answer = 0

arr.sort(reverse=True)

for i in range(len(arr)):
    for j in range(K):
        result.append(arr[0])
    result.append(arr[1])

for i in range(M):
    answer += result[i]

print(answer)