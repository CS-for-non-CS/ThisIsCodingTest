N = int(input())
move = list(input().split())

x = y = 1
direction_x = {'R':1,'L':-1,'D':0,'U':0}
direction_y = {'D':1,'U':-1,'R':0,'L':0}

newx = x
newy = y
for m in move:
    newx = x + direction_x.get(m)
    newy = y + direction_y.get(m)
    if newx > 0 and newx<=N and newy > 0 and newy<=N:
        x = newx
        y = newy

print(y,x)