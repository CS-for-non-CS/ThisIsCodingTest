# deque
from collections import deque

# input
N,K = map(int,input().split())
tube = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())

# 좌표 0부터 시작
X -= 1; Y -= 1

# visit = [[0]*N for _ in range(N)]

# 4방향
dr = [-1,0,1,0]
dc = [0,-1,0,1]

# dic대신 중첩 리스트를 통한 1:N 매칭
start = [[] for _ in range(K+1)]
for r in range(N):
    for c in range(N):
        for i in range(1,K+1):
            if tube[r][c] == i:
                start[i].append([r,c])

# 값이 k 인 start 좌표를 찾아 4방향을 탐색하여 k 값으로 채워넣음
def search(k):
    for _ in range(len(start[k])):
        s = start[k].pop(0)
        r,c = s[0],s[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr == N: continue
            if nc < 0 or nc == N: continue
            if tube[nr][nc] !=0: continue
            tube[nr][nc] = k
            start[k].append([nr,nc])

# S번 반복하며
# K를 1부터 K까지 오름차순으로 search 함수를 호출함
for _ in range(S):
    for k in range(1,K+1):
        search(k)

print(tube[X][Y])

'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
'''
3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''