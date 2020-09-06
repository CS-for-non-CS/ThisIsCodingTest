# 취업을 위한 코딩테스트

## Part 2. 주요 알고리즘 이론과 실전

### Chapter 5. DFS/BFS

---

> 그래프를 탐색하기 위한 대표적인 두 알고리즘



### 꼭 필요한 자료구조 기초

---

* 탐색
  * 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
  * 그래프, 트리 등 자료구조 안에서 알고리즘을 사용하여 탐색
    * 대표적 탐색 알고리즘: DFS, BFS
* 자료 구조
  * 데이터를 표현하고 관리하고 처리하기 위한 구조
  * 자료 구조의 기초
    * 스택과 큐
* 스택과 큐
  * 삽입(Push): 데이터를 삽입
  * 삭제(Pop): 데이터를 삭제
  * 오버 플로
    * 특정 자료 구조의 수용 공간이 이미 데이터로 가득 차 있는 상태에서 삽입 연산 수행 시 발생
    * 저장 공간을 벗어나 데이터가 넘쳐흐를 때
  * 언더플로
    * 특정 자료 구조의 수용 공간에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행 시 발생
    * 저장 공간에 데이터가 없을 때

#### 스택

* 박스 쌓기
  * 아래에서부터 위로 차곡차곡 쌓는 자료 구조
  * 후입 선출(LIFO)
* 파이썬
  * 삽입: append()
  * 삭제: pop()
* 코드 예제

```python
stack = []

# 삽입[5] 삽입[2] 삽입[3] 삽입[7] 삭제 삽입[1] 삽입[4] 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
```



#### 큐

* 줄 서기(대기 줄)
  * 나중에 온 사람이 나중에 들어감
  * '공정한' 자료 구조
  * 선입선출(FIFO)
* 파이썬
  * collections 모듈의 deque 자료구조 활용
    * 스택과 큐의 장점을 모두 채택하였고
    * 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적
    * queue 라이브러리에 비해 간단함
    * list(queue)를 통해 리스트로 자료형 변환 가능
* 코드 예제

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입[5] 삽입[2] 삽입[3] 삽입[7] 삭제 삽입[1] 삽입[4] 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.pop()
queue.append(1)
queue.append(4)
queue.pop()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() #순서 섞기
print(queue[::-1]) #나중에 들어온 원소부터 출력
```



#### 재귀 함수

* 정의
  * 자기 자신을 다시 호출하는 함수
* 최대 깊이
  * 파이썬 인터프리터가 가지고 있는 호출 횟수 제한
  * 재귀 함수를 스택을 이용한 함수처럼 동작하도록 자동 변경하는 라이브러리가 있으나 일반적인 사용 방법은 아니다

* 예제

```python
def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()
    
recursive_function()
```

* 프랙탈
  * 시에르핀스키의 삼각형
  * 프랙탈 구조를 출력할 때 재귀 함수 이용

* 종료 조건

  * 무한 호출을 방지

  ```python
  def recursive_function(i):
      # 100 번째 출력했을 때 종료되도록 종료 조건 명시
      if i == 100:
          return
      print(i,'번째 함수에서',i+1,'번쨰 재귀함수 종료')
      recursive_function(i+1)
      print(i,'번째 재귀함수를 종료합니다')
      
  recursive_function(1)
  ```

  ```
  1 번째 함수에서 2 번쨰 재귀함수 종료
  2 번째 함수에서 3 번쨰 재귀함수 종료
  ...
  99 번째 함수에서 100 번쨰 재귀함수 종료
  99 번째 재귀함수를 종료합니다
  ..
  2 번째 재귀함수를 종료합니다
  1 번째 재귀함수를 종료합니다
  ```

* 구조

  * 재귀 함수의 수행은 스택 자료구조를 이용
  * 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료됨