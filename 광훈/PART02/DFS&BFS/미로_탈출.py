"""
5 6
101010
111111
000001
111111
111111
"""

from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

N -= 1
M -= 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque([[0, 0]])

    # 시작점 방문 처리
    maze[0][0] = 0
    # 방문한 칸 개수
    n = 1

    while True:
        # 이번 턴에 방문할 칸 캐수
        m = len(queue)
        for _ in range(m):
            y, x = queue.popleft()
            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]
                if new_y < 0 or new_y > N:
                    continue
                if new_x < 0 or new_x > M:
                    continue
                if new_y == N and new_x == M:
                    return n + 1
                if maze[new_y][new_x]:
                    queue.append([new_y, new_x])
                    # 방문한 칸 방문 처리
                    maze[new_y][new_x] = 0
        n += 1


result = bfs()
print(result)
