'''
7
2 3 1 2 2 2 2
'''

N = int(input())
arr= list(map(int, input().split()))
temp = []
for i in set(arr):
    temp.append([i,arr.count(i)])
print(temp)
cnt=0
rest=0
portion=0
for i in range(len(temp)):
    portion += rest # 몫
    cnt += (temp[i][1]+ portion) // temp[i][0] #공포지수가 같거나 낮은 사람과 그룹
    rest = temp[i][1] % temp[i][0]
    print(f"i :{i+1} cnt: {cnt} port:{portion}")

print("cnt",cnt)