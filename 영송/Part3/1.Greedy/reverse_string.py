numbers = list(map(int,input()))
n = len(numbers)

count = [0,0]
check = numbers[0]
# 맨 마지막에 남은 숫자가 다른 경우에 카운팅이 되지 않음
for i in range(n-1):
    if numbers[i+1] != check:
        count[numbers[i]] += 1
        check = numbers[i+1]

# 마지막 check 경우의 수를 추가해주기
# 이게 없으면 0101 -> 1이 나옴
count[numbers[n-1]] += 1

print(min(count))