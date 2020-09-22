N,M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
start = []
for r in range(N):
    for c in range(M):
        if lab[r][c] == 2:
            start.append([r,c])
