"""
테스트 케이스만 맞음
"""


def solution(n, build_frame):
    wall_board = [[0] * (n + 1) for _ in range(n + 1)]
    installed = []

    def is_valid_pillar(a, b):
        if b == 0 and wall_board[b + 1][a] == 0:
            return True

        if wall_board[b][a] == 1:
            return True

        if wall_board[b][a] == 3:
            return True

        return False

    def is_valid_bridge(a, b):
        if wall_board[b][a] + wall_board[b][a + 1] == 1:
            return True

        if 3 <= wall_board[b][a] < 6 and 3 <= wall_board[b][a + 1] < 6:
            return True

        if 3 <= wall_board[b][a] < 6 and wall_board[b][a + 1] <= 1:
            return True

        if wall_board[b][a] <= 1 and 3 <= wall_board[b][a + 1] < 6:
            return True

        return False

    for frame in build_frame:
        x = frame[0]
        y = frame[1]

        if frame[2] == 0:
            if frame[3] == 1:
                if is_valid_pillar(x, y):
                    wall_board[y][x] += 1
                    wall_board[y + 1][x] += 1
                    installed.append([x, y, 0])
                    continue
            else:
                if wall_board[y + 1][x] == 1 or wall_board[y + 1][x] >= 6:
                    wall_board[y][x] -= 1
                    wall_board[y + 1][x] -= 1
                    installed.remove([x, y, 0])
        else:
            if frame[3] == 1:
                if is_valid_bridge(x, y):
                    wall_board[y][x] += 3
                    wall_board[y][x + 1] += 3
                    installed.append([x, y, 1])
                    continue
            else:
                if wall_board[y][x] == 0 or wall_board[y][x + 1] == 0:
                    wall_board[y][x] -= 3
                    wall_board[y][x + 1] -= 3
                    installed.remove([x, y, 1])

    return sorted(installed, key=lambda a: (a[0], a[1], a[2]))
