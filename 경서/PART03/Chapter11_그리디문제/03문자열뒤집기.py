'''
연속되는 숫자는 길이와 상관없이 묶임
앞뒤로 다른 숫자가 등장하면 뒤집어야함
'''

N=input()
result = 1
target = N[0] #0,1
for i in range(1, len(N)):
    if N[i] != target: #처음 등장하는 숫자와 다른 경우
        target = N[i]
        result += 1
print(result//2)
