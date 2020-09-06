n=1260
coin = [500,100, 50, 10]
total = [0] *len(coin)

for i in range(len(coin)):
    total[i] = n//coin[i]
    n %= coin[i]

print(total)