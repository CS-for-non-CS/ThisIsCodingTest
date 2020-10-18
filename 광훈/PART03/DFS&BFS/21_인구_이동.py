from collections import deque

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(r, c):
    queue = deque([[r, c]])

    visited[r][c] = 1
    group = [[r, c]]
    group_sum = countries[r][c]

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]

            if new_y < 0 or new_y >= N:
                continue

            if new_x < 0 or new_x >= N:
                continue

            diff = abs(countries[new_y][new_x] - countries[y][x])

            if not visited[new_y][new_x] and L <= diff <= R:
                queue.append([new_y, new_x])
                group.append([new_y, new_x])
                group_sum += countries[new_y][new_x]
                visited[new_y][new_x] = 1

    if len(group) == 1:
        return False

    new_value = group_sum // len(group)

    for country in group:
        y, x = country
        countries[y][x] = new_value

    return True


flag = 0
result = 0

while True:
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                grouping = bfs(i, j)
                if grouping:
                    flag = 1

    if not flag:
        break

    flag = 0
    result += 1
    visited = [[0] * N for _ in range(N)]

print(result)
