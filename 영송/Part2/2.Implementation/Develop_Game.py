#N,M을 공백으로 구분하여 입력받기
N,M = map(int,input().split())

# 방문한 위치 정보를 저장하기 위한 맵
visit = [[0]*M for _ in range(N)]

#현재 캐릭터의 X좌표, Y좌표, 방향 입력
r, c, d = map(int,input().split())
visit[r][c] = 1 # 현재 좌표 방문처리

# 전체 맵 정보 입력받기
maps = [list(map(int,input().split())) for _ in range(N)]

# 북,동,남,서 방향에서의 전진 정의
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽 회전
    turn_left()
    nr = r + dr[d]
    nc = c + dc[d]
    # 회전 후 정면에 가보지 않은 칸이 존재하면 이동
    if visit[nr][nc] == 0 and maps[nr][nc] == 0:
        visit[nr][nc] = 1
        r = nr
        c = nc
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nr = r-dr[d]
        nc = c-dc[d]
        # 뒤로 갈 수 있다면 이동
        if maps[nr][nc] == 0:
            r = nr
            c = nc
        #뒤로 바다로 막힌 경우
        else:
            break
        turn_time = 0

print(count)