N,M = 15, 14
tray = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def check(x,y):
    if x<0 or x == N: return False
    if y<0 or y == M: return False
    if tray[x][y] == 1: return False
    if visited[x][y] == 1: return False
    return True

def dfs(v):
    r = v[0]; c=v[1]
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]; nc = c + dc[i]
        if check(nr,nc):
            dfs([nr,nc])

cnt = 0
for r in range(N):
    for c in range(M):
        if not tray[r][c] and not visited[r][c]:
            dfs([r,c])
            cnt += 1
print(cnt)