"""
효율성 통과 아직 못했음
"""


def solution(food_times, k):
    i = 0
    result = 0
    indexes = [x for x in range(len(food_times))]

    while k > 0:
        food_times[indexes[i]] -= 1
        if food_times[indexes[i]] == 0:
            del indexes[i]
        else:
            i += 1

        if len(indexes) == 0:
            result = -1
            break

        k -= 1
        i %= len(indexes)

    if result != -1:
        result = indexes[i] + 1

    return result
