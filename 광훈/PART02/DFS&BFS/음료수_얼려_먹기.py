"""
4 5
00110
00011
11111
00000
"""

# N: 행, M: 열, ices: 얼음판
N, M = map(int, input().split())
ices = [list(input()) for _ in range(N)]

result = 0
visited = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        # 인덱스 범위 검사
        if new_y < 0 or new_y >= N:
            continue

        if new_x < 0 or new_x >= M:
            continue

        if visited[new_y][new_x] == 0 and ices[new_y][new_x] == '0':
            dfs(new_y, new_x)


for r in range(N):
    for c in range(M):
        if not visited[r][c] and ices[r][c] == '0':
            dfs(r, c)
            result += 1

print(result)
