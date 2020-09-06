'''
5
R R R U D D
'''
N = int(input())
arr = list(input().split())
X = Y = 1

def check(T):
    if T < 1 or T==N :return True
    return False

for i in range(len(arr)):
    if arr[i] == "R":
        if check(Y+1): continue
        Y += 1
    elif arr[i] == "D":
        if check(X+1): continue
        X += 1
    elif arr[i] == "L":
        if check(Y-1): continue
        Y -= 1
    else: #U
        if check(X-1): continue
        X -= 1
print(X,Y)