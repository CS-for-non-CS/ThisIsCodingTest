N = int(input())
coins = list(map(int, input().split()))
coins.sort()

i = 1

while True:
    possible = False

    def is_possible(index, cur_sum):
        global possible
        global i

        if cur_sum == i:
            possible = True
            return

        if index == N or cur_sum > i:
            return

        is_possible(index+1, cur_sum+coins[index])
        is_possible(index+1, cur_sum)

    is_possible(0, 0)

    if not possible:
        break

    i += 1

print(i)
