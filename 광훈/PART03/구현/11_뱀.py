"""
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""

from collections import deque

# N: 보드의 크기, K: 사과의 개수
N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

# L: 뱀의 방향 전환 횟수
L = int(input())
dir_changes = [input().split() for _ in range(L)]

board = [[0] * N for _ in range(N)]
board[0][0] = 1

# 사과 위치 표시
for apple in apples:
    board[apple[0]-1][apple[1]-1] = 2

# second: 현재 시간, direction: 현재 방향, change_index: dir_changes 인덱스
# x: 현재 x 좌표, y: 현재 y 좌표
second = direction = change_index = x = y = 0

# 방향 전환 위한 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 뱀 현재 위치들
snake = deque()
snake.append([0, 0])


# 벽에 닿았는지 검사
def out_of_range(a):
    if a < 0 or N <= a:
        return True
    return False


while True:
    # 현재 시간 +1
    second += 1

    # 다음에 갈 좌표
    new_x = x + dx[direction]
    new_y = y + dy[direction]

    # 벽 만나면 break
    if out_of_range(new_x) or out_of_range(new_y):
        break

    # 자기 몸통이면 break
    if board[new_y][new_x] == 1:
        break
    else:
        # 사과가 없을 경우 맨 뒤에 놈이 없어짐
        if board[new_y][new_x] == 0:
            tail_y, tail_x = snake.pop()
            board[tail_y][tail_x] = 0
        snake.appendleft([new_y, new_x])
        board[new_y][new_x] = 1

    # 현재 위치 변경
    x = new_x
    y = new_y

    # 방향 전환 검사
    if change_index < L and dir_changes[change_index][0] == str(second):
        # 왼쪽일 때
        if dir_changes[change_index][1] == 'L':
            direction -= 1
        # 오른쪽일 때
        else:
            direction += 1
        # 인덱스 벗어날 경우 대비
        direction %= 4
        # 다음 dir_changes 인덱스 검사
        change_index += 1

print(second)
