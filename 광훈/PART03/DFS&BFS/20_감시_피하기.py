N = int(input())
hallway = [input().split() for _ in range(N)]

students = []
empties = []

# 학생과 빈 칸 리스트 구축
for r in range(N):
    for c in range(N):
        if hallway[r][c] == 'S':
            students.append([r, c])
        if hallway[r][c] == 'X':
            empties.append([r, c])


# 장애물 세 개 배치했을 때 유효한 건지 확인
def is_valid():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for student in students:
        y, x = student
        for d in range(4):
            new_y = y + dy[d]
            new_x = x + dx[d]
            # 리스트 범위 벗어나는지 확인
            while 0 <= new_x < N and 0 <= new_y < N:
                # 선생님 만나면 유효하지 않은 것
                if hallway[new_y][new_x] == 'T':
                    return False

                # 장애물 만나면 패스
                if hallway[new_y][new_x] == 'O':
                    break

                # 한 칸 더 감
                new_y += dy[d]
                new_x += dx[d]
    return True


# 장애물 세우기
def make_obstacle():
    n = len(empties)
    # 장애물 세울 빈 칸 3개 고르기
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                r1, c1 = empties[i]
                r2, c2 = empties[j]
                r3, c3 = empties[k]

                hallway[r1][c1] = 'O'
                hallway[r2][c2] = 'O'
                hallway[r3][c3] = 'O'

                if is_valid():
                    return 'YES'

                hallway[r1][c1] = 'X'
                hallway[r2][c2] = 'X'
                hallway[r3][c3] = 'X'

    return 'NO'


result = make_obstacle()
print(result)
