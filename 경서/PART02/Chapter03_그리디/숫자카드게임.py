'''
3 3
3 1 2
4 1 4
2 2 2
'''
'''
2 4
7 3 1 8
3 3 3 4
'''
N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
for i in arr:
    if max_num < min(i):
        max_num = min(i)
print(max_num)