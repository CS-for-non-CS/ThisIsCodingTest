position = input()
c = ord(position[0]) - ord('a')
r = int(position[1]) - 1

dr = [-2, -2, 2, 2, -1, 1, -1, 1]
dc = [-1, 1, -1, 1, -2, -2, 2, 2]

cnt = 0

for i in range(8):
    nc = c+dc[i]
    nr = r+dr[i]
    if nc >= 0 and nc < 8 and nr >=0 and nr < 8:
        cnt += 1

print(cnt)
