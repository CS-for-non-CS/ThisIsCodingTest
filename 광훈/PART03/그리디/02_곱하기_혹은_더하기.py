S = input()

result = 0

for s in S:
    if result == 0:
        result += int(s)
    else:
        if int(s) == 1:
            result += int(s)
        elif int(s):
            result *= int(s)

print(result)
