S = input()

state = S[0]
nums = [0, 0]

for s in S:
    if s != state:
        nums[int(state)] += 1
        state = s

nums[int(state)] += 1

print(min(nums))
