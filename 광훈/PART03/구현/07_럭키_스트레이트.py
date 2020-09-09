N = input()

# 중간 인덱스
middle = len(N) // 2

# 왼쪽 합, 오른쪽 합
left_sum = 0
right_sum = 0

# 왼쪽 합 구하기
for num in N[:middle]:
    left_sum += int(num)

# 오른쪽 합 구하기
for num in N[middle:]:
    right_sum += int(num)

# 같은 지 비교
if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
