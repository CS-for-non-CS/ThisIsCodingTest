N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_value = 1000000000
max_value = -1000000000


# a1: 숫자1, a2: 숫자2, i: 연산자 인덱스
def calculate(a1, a2, i):
    # 덧셈
    if i == 0:
        return a1 + a2

    # 뺄셈
    if i == 1:
        return a1 - a2

    # 곱셈
    if i == 2:
        return a1 * a2

    # 나눗셈 0 체크
    if a2 == 0:
        return 'error'

    # 일단 둘 다 양수로 바꿔서 나눗셈 계산
    divide_value = abs(a1) // abs(a2)

    # a1이 음수일 경우 음수 반환, a2도 체크해줘야 할 것 같은데... 그냥 통과됐음
    return divide_value if a1 >= 0 else -divide_value


def dfs(n, k):
    global min_value, max_value

    # 모든 숫자를 연산했을 때
    if k == len(numbers):
        min_value = min(min_value, n)
        max_value = max(max_value, n)

    for index, operator in enumerate(operators):
        if operator:
            new_n = calculate(n, numbers[k], index)
            # 나눗셈 에러 났을 경우
            if new_n == 'error':
                continue
            operators[index] -= 1
            dfs(new_n, k + 1)
            operators[index] += 1


dfs(numbers[0], 1)

print(max_value)
print(min_value)
