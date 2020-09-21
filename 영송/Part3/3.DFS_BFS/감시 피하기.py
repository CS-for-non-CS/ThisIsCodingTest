N = int(input())
room = [list(input().split()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

student = []
for r in range(N):
    for c in range(N):
        if room[r][c] == 'T':
            student.append([r,c])

cnt = 0
def search(i):
    r,c = student[i][0], student[i][1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        while nr>=0 and nr!=N and nc>=0 and nc!=N and room[nr][nc] != 'T':
            nr += dr[i]
            nc += dc[i]
        if nr <0 or nr == N:continue
        if nc <0 or nc == N:continue
        if room[nr][nc] == 'T':
            while room[r][c] != 'T':
                room[r+dr[i]][c+dc[i]] = 'O'
            cnt += 1



