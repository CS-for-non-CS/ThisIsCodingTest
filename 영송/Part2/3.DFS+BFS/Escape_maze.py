from collections import deque

N,M = 5,6
maze = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# r,c = N,M 종료

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def check(x,y):
    if x < 0 or x == N: return False
    if y < 0 or y == M: return False
    if visited[x][y] != 0: return False
    if maze[x][y] == 0: return False
    return True

def BFS(v):
    sr = v[0]; sc = v[1]
    Q = deque()
    Q.append([sr,sc])
    visited[sr][sc] = 1
    while len(Q):
        q = Q.popleft()
        r = q[0]; c = q[1]
        if (r, c) == (N - 1, M - 1):
            return visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if check(nr,nc):
                Q.append([nr,nc])
                visited[nr][nc] = visited[r][c] + 1

print(BFS((0,0)))