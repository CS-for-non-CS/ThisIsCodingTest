N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
stores = []

# 최대값 잘 설정해주어야 함
result = (N ** 3) * 2

# 집, 치킨 집 좌표 추가
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i + 1, j + 1])
        elif city[i][j] == 2:
            stores.append([i + 1, j + 1])


# M개의 치킨 집을 골랐을 때 거리합 구하는 함수
def get_min(store_list):
    total = 0
    for house in houses:
        house_min = N * 2
        for store in store_list:
            house_min = min(house_min, abs(house[0] - store[0]) + abs(house[1] - store[1]))
        total += house_min
    return total


# M개의 치킨 집을 고르는 함수
def dfs(k, store_list):
    global result

    if len(store_list) == M:
        result = min(result, get_min(store_list))
        return

    if len(stores) <= k:
        return

    store_list.append(stores[k])
    dfs(k + 1, store_list)
    store_list.pop()
    dfs(k + 1, store_list)


dfs(0, [])

print(result)
