[toc]

# 취업을 위한 코딩테스트

## Part 2. 주요 알고리즘 이론과 실전

### Chapter 3. 그리디

---

> 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘

* 정의
  * 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘
  * '탐욕적'
    * **`현재 상황에서 지금 당장 좋은 것만 고르기`**
* 유형
  * **`사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제`**
  * 일부 다익스트라와 같이 '사전 암기'가 필요한 유형도 존재하지만 대체로 그리디 알고리즘은 출제의 폭이 매우 넓음
* 대비
  * 단순 암기로 모든 문제를 대처하기 어려움
  * 많은 유형을 접해보고 훈련이 필요함
* 풀이법
  * 창의력
    * 문제를 풀기 위한 최소한의 아이디어를 떠올리는 능력
  * 단순히 현재 상황에서 가장 좋아 보이는 것만 선택해도        전체 문제를 풀 수 있는지 파악이 필요
    * 보통 '기준'에 따라 좋은 것을 선택하는 유형
    * 정렬 알고리즘과 자주 짝을 이루어 출제됨

##### [예제: 거스름돈]

* 문제상황
  * N원을 거스름돈으로 줄 때
    * 단, N은 10의 배수
  * {500, 100, 50, 10}의 단위를 사용하여
  * 거슬러줘야 할 동전의 최소 개수

* 문제해설

  * 가장 큰 단위의 동전과 가장 작은 단위의 동전의 관계 파악

    * 만약, 화폐 단위가 500, 400, 100, 10으로 주어진 경우
    * N = 800원을 거슬러줄 때
    * 가장 큰 단위의 동전으로 출발하게 되면
    * 500 + 100 + 100 + 100: 3개
    * 400+400 = 2개
    * **`이 경우 가지고 있는 동전의 큰 단위가 항상 작은 단위의 배수가 아니므로 작은 단위의 동전을 종합해 다른 해가 나올 가능성이 존재함`**

  * {500,100,50,10}은 서로 약수/배수 관계

    * '가장 큰 단위의 화폐부터 가장 작은 단위의 화폐까지 차례대로 확인하여 거슬러 주는 작업만을 수행하면 된다'
    * Becase: 작은 것은 어떻게 조합해도 큰 것이 되기 때문

  * 코드

    ```python
    n = 1260
    count = 0
    
    #리스트의 배열 순서 = 최적 해 탐색 순서, 크기 순
    coin_list = [500,100,50,10]
    
    #동전의 개수를 셀 때, 몫과 나머지를 이용
    for coin in coin_list:
        cnt += n // coin 
        n %= coin
    
    print(count)
    ```

* 시간 복잡도

  * 리스트의 원소 개수를 K라고 할 떄,
  * 리스트의 원소만큼 나눗셈-몫, 나눗셈-나머지를 계산하므로
  * 빅O기준, O(K)
    * N의 크기는 시간 복잡도에 미치는 영향이 없다



### 실전 문제: 큰 수의 법칙

---

다양한 수로 이루어진 배열이 주어질 때 주어진 수들을 M번 더하여 가장큰 수를 만들고자 한다. 단, 배열의 특정한 인덱스(번호)를 K번 연속해서 더할 수 없는 것이 제약 사항이다.

예를 들어 순서대로 2,4,5,4,6이라는 배열이 주어지고, M은 8, K는 3이라고 가정하자. 이 경우 특정 인덱스의 수가 연속해서 세 번 까지만 더해질 수 있으므로 큰 수의 버빅에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46이 된다.

단, 서로 다른 인덱스를 가졌으나 인덱스에 해당하는 값이 동일한 경우에는 서로 다른 것으로 간주할 수 있다. 예를 들어 순서대로 3,4,3,4,3 으로 이루어진 배열이 있을 때 M=7, K=2라고 가정하자. 이 경우 두 번째 원소 4와 네 번째 원소 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4 + 4+ 4+ 4+ 4+ 4 + 4 = 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때의 결과를 출력하시오.

`입력 조건`

* 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
* 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
* 입력으로 주어지는 K는 항상 M보다 작거나 같다.

`출력 조건`

* 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

`입력 예시`

```
5 8 3
2 4 5 4 6
```

`출력 예시`

```
46
```

`My코드`

```python
N, M , K = map(int,input().split())
numbers = list(map(int,input().split()))

max_idx = 0
for i in range(N):
    if numbers[max_idx] < numbers[i]:
        max_idx = i

sec_idx = 0
for i in range(N):
    if i != max_idx:
        if numbers[i] > numbers[sec_idx]:
            sec_idx = i

total = 0
cnt = 0
check = 0
while cnt != M:
    if check <K:
        total += numbers[max_idx]
        cnt += 1
        check += 1
    elif check == K:
        total += numbers[sec_idx]
        cnt += 1
        check = 0

print(total)
```

`NDB코드`

```python
n, m, k = map(int,input().split())
data = list(map(int,input().split()))

#정렬 내장함수 사용
data.sort()
first = data[n-1] #n-1이 마지막 인덱싱
second = data[n-2]

result = 0

while True:
    for i in range(k):  #가장 큰 수 K번 더하기
        if m == 0:      #m이 0 일때 결과값 도출하기 위해
            break
        result += first
        m -= 1         #더할 때 마다 m은 1씩 감소
    if m == 0:         #m이 0이라면 반복문 탈출
        break
    result += second # 큰 수를 k번 반복한 후 한 번 더하기
    m -= 1

print(result)
```

`Good Practice`

> 시행을 1회씩 거듭하여 계산을 누적하는 방식은 M의 크기에 따라 시간 제한 문제에 빠질 수 있다.
>
> 따라서 반복되는 패턴을 파악하여 보다 시간 복잡도를 줄이는 방식을 생각해 볼 수 있다. 
>
> 이 경우 반복 패턴은 K+1의 주기로 이루어지며, 
> 반복값은 max * first_count + second 로 주어진다.

```python
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
```



### 실전문제: 숫자 카드 게임

---

숫자 카드 게임은 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 단, 게임의 룰은 아래와 같다.

1. 숫자 카드는 N X M의 형태이다. 이 때 N은 행의 개수, M은 열의 개수를 의미한다.
2. 행을 선택한다.
3. 선택된 행의 카드 중 가장 숫자가 낮은 카드를 뽑는다.
4. 처음 카드를 골라낼 행을 선택할 때, 각 행들의 가장 낮은 숫자들 중 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

예를 들어, 3 X 3 형태의 카드가 다음과 같이 놓여있다.

| 행\열 | 0    | 1    | 2    |
| ----- | ---- | ---- | ---- |
| 0     | 3    | 1    | 2    |
| 1     | 4    | 1    | 4    |
| 2     | 2    | 2    | 2    |

0행과 1행을 고르는 경우 1을 뽑게 되고, 2행을 고르는 경우 2를 뽑게 되므로 2행을 고르는 것이 정답니다.

카드가 N X M 형태로 주어질 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 작성하시오.

`입력 조건`

* 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N,M <=100)

* 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.

`출력 조건`

* 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

`입력예시`

```
3 3 
3 1 2
4 1 4
2 2 2
2 4 
7 3 1 8
3 3 3 4
```

`출력 예시`

```
2
3
```

`My코드`

```python
N, M = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(N)]

#먼저 각 행별로 가장 낮은 숫자를 비교하기 위해 초기값을 설정
low = cards[0][0]
for i in range(M):
    if cards[0][i] < low:
        low = cards[0][i]

# 각 행의 모든 숫자를 탐색하여 낮은 숫자를 low_idx로 찾고
# 찾은 low_idx를 앞서 구한 low와 비교하여 높은 숫자 획득
for n in range(N):
    low_idx = 0
    for m in range(M):
        if cards[n][m] < cards[n][low_idx]:
            low_idx = m
    if cards[n][low_idx] > low:
        result = n
        low = cards[n][low_idx]

# result의 경우 몇 행을 선택하는지 추가해준 답안        
print(result,low)
```

`NDB코드`

> 문제의 아이디어
>
> > **각 행마다 가장 작은 수를 찾은 뒤, 그 수 중 가장 큰 수 찾기**
>
> 요구 스킬
>
> > min()
> >
> > 2중 for문

```python
#min()
n,m = map(int,input().split())

result = 0
# 행을 한 줄씩 입력 받으며 확인함
for i in range(n):
    data = list(map(int,input().split()))
    #가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수 중에서 가장 큰 수 찾기
    result = max(result,min_value)

print(result)
```

```python
#2중 for문
n,m = map(int,input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = 1001
    for number in data:
        min_value = min(min_value,number)
    result = max(result,min_value)

print(result)
```



### 실전 문제: 1이 될 때까지

---

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 

1. N에서 1을 뺀다.

2. N을 K로 나눈다.

   단, 2의 경우, N이 K로 나누어 떨어질 때만 선택할 수 있다.

예를 들어 N이 17, K가 4라고 가정하자. 이 때 1을 수행하면 N은 16이다. 이후 2를 두 번 수행하면 N이 1이 왼다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이다. 이는 N을 1로 만드는 최소 횟수이다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

`입력조건`

* 첫째 줄에 N(2 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

`출력조건`

* 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최소값을 출력한다.

`입력 예시`

```
17 4
25 5
```

`출력 예시`

```
3
2
```

`My 코드`

```python
N, K = map(int,input().split())

cnt = 0
while N != 1:
    # K로 나눌 수 있는지 검사, K는 1보다 크다!
    if N % K ==0:
        # 나누기 연산자는 float을 반환하므로 몫 연산
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)
```

`NDG코드`

> 아이디어
>
> > 최대한 많은 나누기 유도
>
> 검증
>
> >  단, K가 2이상의 정수이기 때문에 가능한 방법
> >
> > 빼기의 경우도 N이 커지는 경우 시간 제한을 받게 된다.

```python
# 시행마다 빼기를 반복
n,k = map(int,input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n>=k:
    #N이 K로 나누어 떨어지지 않으면 N에서 1 뺴기
    while n % k != 0:
        n -= 1
        result += 1
    #K로 나누기
    n //= k
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -= 1
    result += 1

print(result)
```

```python
# k를 기준으로 뺄셈 횟수를 한 번에 계산

n,k = map(int,input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) break
    if n < k:
        break
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1) # n - (n-1) = 1
print(result)
```


