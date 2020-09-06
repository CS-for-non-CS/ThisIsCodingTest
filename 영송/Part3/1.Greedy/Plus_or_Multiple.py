
numbers = list(map(int,input()))
n = len(numbers)


total = 0
for i in range(n):
    # total == 0의 경우의 수가 더 작기 때문에 컴퓨터가 읽을 문장의 개수가 많아짐
    if total == 0:
        total += numbers[i]
    else:
        # +1 생각 못함
        if numbers[i] == 0 or numbers[i] == 1:
            total += numbers[i]
        else:
            total *= numbers[i]

print(total)