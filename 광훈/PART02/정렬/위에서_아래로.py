N = int(input())
array = [int(input()) for _ in range(N)]

for x in sorted(array, reverse=True):
    print(x, end=' ')
