# 우선순위 큐 모듈
import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    # 총 시간
    sum_value = 0
    # 직전에 다 먹은 시간
    previous = 0
    # 남은 음식의 개수
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    # 한 음식을 검사할 때마다 사이클을 도는 것으로 이해하면 된다
    # 몇 사이클 째 k번째 음식이 나오는지 구하는 식
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # 음식 시간이 작은 놈부터 나오는 것 같다
        now = heapq.heappop(q)[0]
        # 현재 음식을 다 먹기 위해서 몇 사이클을 돌아야 하는지 구하고 더해준다
        sum_value += (now - previous) * length
        # 현재 음식을 다 먹었기 때문에 길이가 1 줄었다
        length -= 1
        # 이전 음식 시간 재설정
        previous = now

    # 음식 번호를 기준으로 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
