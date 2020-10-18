"""
5 3
1 2 5 4 3
5 5 6 6 5
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while K > 0:
    min_a = max_b = 0

    for i in range(N):
        if A[min_a] > A[i]:
            min_a = i
        if B[max_b] < B[i]:
            max_b = i

    if A[min_a] >= B[max_b]:
        break

    A[min_a], B[max_b] = B[max_b], A[min_a]
    K -= 1

print(sum(A))
