"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""

"""
3 3
1 0 2
0 0 0
3 0 0
1 2 2
"""

N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

s = 0
no_virus = []

for r in range(N):
    for c in range(N):
        if not array[r][c]:
            no_virus.append([r, c, 0])


def my_virus(y, x):
    virus = 0
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y >= N:
            continue
        if new_x < 0 or new_x >= N:
            continue
        if array[new_y][new_x]:
            if virus == 0:
                virus = array[new_y][new_x]
            else:
                virus = min(virus, array[new_y][new_x])
    return virus


while s < S and len(no_virus) and not array[X - 1][Y - 1]:
    for room in no_virus:
        room[2] = my_virus(room[0], room[1])

    new_no_virus = []

    for room in no_virus:
        if room[2]:
            array[room[0]][room[1]] = room[2]
        else:
            new_no_virus.append(room)

    s += 1

print(array[X - 1][Y - 1])
