"""
4 4 1 1
1 2
1 3
2 3
2 4
"""

from collections import deque

N, M, K, X = map(int, input().split())

# 인접 리스트
cities = [[] for _ in range(N + 1)]

for _ in range(M):
    city1, city2 = map(int, input().split())
    cities[city1].append(city2)

# 도시별 경로
num_of_paths = [-1] * (N + 1)
# 출발점 0으로 초기화
num_of_paths[X] = 0


def bfs():
    queue = deque([X])
    while queue:
        cur_city = queue.popleft()
        for city in cities[cur_city]:
            # -1이면 방문한 적이 없는 도시
            if num_of_paths[city] == -1:
                # 현재 방문한 도시의 경로 + 1
                num_of_paths[city] = (num_of_paths[cur_city] + 1)
                queue.append(city)


bfs()

result = []

# 경로의 길이가 K인 도시들 찾기
for index, path in enumerate(num_of_paths):
    if path == K:
        result.append(index)

# 도시가 없을 때 -1 넣기
if not len(result):
    result.append(-1)

for c in result:
    print(c)
