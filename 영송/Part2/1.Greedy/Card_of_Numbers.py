N, M = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(N)]

low = cards[0][0]
for i in range(M):
    if cards[0][i] < low:
        low = cards[0][i]

for n in range(N):
    low_idx = 0
    for m in range(M):
        if cards[n][m] < cards[n][low_idx]:
            low_idx = m
    if cards[n][low_idx] > low:
        result = n
        low = cards[n][low_idx]

print(result,low)