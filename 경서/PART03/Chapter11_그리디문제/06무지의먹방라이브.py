K = 7
food_times = [3,1,2]


from collections import deque

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    Q = deque()
    for i in range(len(food_times)):
        Q.append([food_times[i],i+1])
    print(Q)
    for i in range(k):
        D, idx = Q.popleft()
        if D == 1: continue
        else:
            Q.append([D-1, idx])
    answer = Q[0][1]
    return answer

print(solution(food_times, K))