N, M, K = map(int,input().split())
numbers = list(map(int,input().split()))

numbers.sort()
first = numbers[N-1]
second = numbers[N-2]

first_count = K * (M//(K+1)) + M % (K+1)
second_count = M - first_count

result = 0
result += first * first_count + second * second_count

print(result)