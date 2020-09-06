N, M , K = map(int,input().split())
numbers = list(map(int,input().split()))

max_idx = 0
for i in range(N):
    if numbers[max_idx] < numbers[i]:
        max_idx = i

sec_idx = 0
for i in range(N):
    if i != max_idx:
        if numbers[i] > numbers[sec_idx]:
            sec_idx = i

total = 0
cnt = 0
check = 0
while cnt != M:
    if check <K:
        total += numbers[max_idx]
        cnt += 1
        check += 1
    elif check == K:
        total += numbers[sec_idx]
        cnt += 1
        check = 0

print(total)