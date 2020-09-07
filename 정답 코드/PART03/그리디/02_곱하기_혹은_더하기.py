data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])

    # 스터디에서는 합이 1인 경우를 간과했음 합이 1일 경우 무조건 더하는 게 이득
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
