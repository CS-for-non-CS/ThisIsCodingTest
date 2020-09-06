#n = int(input())

# count = 0
# for h in range(n+1):
#     for m in range(60):
#         for s in range(60):
#             #매 시각 안에 '3'이 포함된 경우를 찾아 카운트 증가
#             if '3' in str(h) + str(m) + str(s):
#                 count += 1

# print(count)

n = int(input())

def check(h,m,s):
    result = 0
    if s // 10 == 3 or s % 10 == 3 or m // 10 == 3 or m % 10 == 3 or h % 10 == 3:
        result = 1
    return result

total = (n+1) * (60**2)

cnt = 0
h = m = s = 0
for i in range(total):
    h = i // 60**2
    m = (i % 60**2) // 60
    s = i % 60

    cnt += check(h,m,s)

print(cnt)