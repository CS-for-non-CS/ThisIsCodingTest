"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸, 바이러스 칸
empty_room = []
virus_room = []

# 빈 칸, 바이러스 칸 인덱스 리스트에 추가
for r in range(N):
    for c in range(M):
        if lab_map[r][c] == 0:
            empty_room.append([r, c])
        if lab_map[r][c] == 2:
            virus_room.append([r, c])


# 원래 지도로 초기화하기
def initiate_map():
    for room in empty_room:
        lab_map[room[0]][room[1]] = 0


# 세 점에 벽 세우기
def make_walls(w1, w2, w3):
    r1, c1 = empty_room[w1]
    r2, c2 = empty_room[w2]
    r3, c3 = empty_room[w3]

    lab_map[r1][c1] = 1
    lab_map[r2][c2] = 1
    lab_map[r3][c3] = 1


# 바이러스 증식 (dfs)
def spread_virus(y, x):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for t in range(4):
        new_y = y + dy[t]
        new_x = x + dx[t]

        if new_x < 0 or new_x >= M:
            continue

        if new_y < 0 or new_y >= N:
            continue

        # 빈 칸일 경우 바이러스로 바꿈
        if lab_map[new_y][new_x] == 0:
            lab_map[new_y][new_x] = 2
            spread_virus(new_y, new_x)


# 바이러스가 퍼진 후, 빈 칸 개수 구하기
def get_empty_room():
    total = 0
    for r in range(N):
        for c in range(M):
            if lab_map[r][c] == 0:
                total += 1
    return total


# n: 빈 칸의 개수
n = len(empty_room)
result = 0

# 3개의 빈 칸 조합 모두 찾아서 넣기
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            initiate_map()
            make_walls(i, j, k)
            for room in virus_room:
                spread_virus(room[0], room[1])
            result = max(result, get_empty_room())

print(result)
