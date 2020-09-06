'''
5
3 2 1 1 9
3
3 5 7
3
1 2 4
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print("arr:", arr)
result = 1
for i in arr:
    print("i:", i, "result:", result)
    if i > result: break
    else:
        result += i

print(result)

