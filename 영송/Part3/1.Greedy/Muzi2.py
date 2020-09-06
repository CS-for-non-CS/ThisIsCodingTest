def solution(food_times, k):
    n = len(food_times)
    s = k//n
    if k <= n:
        answer = k % n + 1
    else:

    return answer

food_times=[3,1,2]
k = 5
print(solution(food_times,k))
