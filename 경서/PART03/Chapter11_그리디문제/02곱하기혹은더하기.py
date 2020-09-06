'''
02984
'''

N=input()
result = 0
if len(N) == 1: print(N)
else:
    start= int(N[0])
    if start == 0:
        for i in range(1,len(N)):
            if int(i) == 0: continue
            elif result == 0 :
                result += int(N[i])
            else: result *= int(N[i])
    else:
        for i in range(len(N)):
            if result == 0: result = int(N[i])
            else: result *= int(N[i])
print(result)

'''
0/1/9/0/8/3/6/4
1/2/3
'''