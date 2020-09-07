data = input()

# 0으로 바꾸는 경우
count0 = 0
# 1로 바꾸는 경우
count1 = 0

# 첫 번째 원소에 대해서 처리
# 답안에서는 마지막 원소를 더해주지 않고 처음에 더해주는 걸로 모든 원소를 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수가 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수가 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
