N = int(input())
fear = list(map(int,input().split()))

# 공포 지수의 최대 값 찾기
max_idx = 0
for i in range(N):
    if fear[i] > fear[max_idx]:
        max_idx = i

# 카운트 배열을 통해 각 공포수치 마다 사람 수 세기
count = [0] * (fear[max_idx]+1)
for i in range(N):
    count[fear[i]] += 1

# 그리디, 앞에서부터
# 나머지 넘기지 않음
total = 0
rest = 0
l = len(count)
for i in range(1,l):
    total += (count[i]+rest)//i
    rest += count[i] % i
print(total)