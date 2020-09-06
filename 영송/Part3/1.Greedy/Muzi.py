def solution(food_times, k):
    n = len(food_times)
    # while 사용으로 바꾸기
    # k가 food_times의 sum 보다 큰 케이스에 대한 예외 처리
    # 반복 시행 후 k와 food_times sum 값을 비교하는 것보다
    # 시행 초기에 값의 대수 비교
    for i in range(k+1):
        # 만약, while 을 사용시, n은 고정시켜야 함
        # food_times에서 원소를 삭제시키면 본래 index 정보가 사라짐
        i %= n
        # i번째 횟수에 foot times가 감소하지 않으므로
        # while로 바꿔서 else인 경우 i를 업데이트 하도록 변경
        if food_times[i] == 0:
            continue
        else:
            food_times[i] -= 1

    answer = food_times[(k+1)//n]+1

    return answer

food_times=[3,1,2]
k = 5
print(solution(food_times,k))
