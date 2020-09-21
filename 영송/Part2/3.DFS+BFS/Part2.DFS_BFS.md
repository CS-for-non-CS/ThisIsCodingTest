[toc]

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
  * 대표적 예시: DFS
  
* 팩토리얼

  * 0!과 1!은 모두 1의 값을 가짐

  ```python
  # 반복 팩토리얼 n!
  def factorial_iterative(n):
      result = 1
      # 1부터 n까지 차례로 곱하기
      for i in range(1,n+1):
          result += i
      return result
  
  # 재귀적 n!
  def factorial_recursive(n):
      if n<=1:	#n이 1이하인 경우 1을 반환
          return 1
     	# n! = n* (n-1)을 코드로 작성
      return n * factorial_recursive(n-1)
  ```

  * 반복의 방식과 재귀의 방식 모두 120번의 연산을 수행함

* 재귀의 장점

  * 코드가 간결함
  * 다이나믹 프로그래밍 이용 가능
  * 점화식



### 탐색 알고리즘 DFS/BFS

---

#### DFS

> Depth-First Search
>
> 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

##### 그래프(Graph)

* 그래프는 노드와 간선으로 표현
  * 이 때 노드는 정점(Vertex)로 표현
  * 두 노드가 간선으로 연결되어 있다면 두 노드는 '인접하다'(Adjacent)
* 그래프 탐색이란?
  * 하나의 노드를 시작으로 다수 노드를 방문하는 것

##### 그래프 표현방식

* 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계 표현
* 인접 리스트(Adjacency List): 다차원 리스트로 그래프의 연결 관계 표현

##### 예시

> From `0` to `1`, 간선 비용 7
>
> From `0` to `2`, 간선 비용 5

* 인접 행렬

  |      | 0    | 1    | 2    |
  | ---- | ---- | ---- | ---- |
  | 0    | 0    | 7    | 5    |
  | 1    | 7    | 0    | 무한 |
  | 2    | 5    | 무한 | 0    |

  * 인접 행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록함
  * 연결되지 않은 노드에 대한 정보는 무한(INFinity)의 비용을 작성

  ```python
  INF = 999999999 #무한 비용 선언
  
  # 2차원 리스트를 이용한 인접 행렬 표현
  graph = [
      [0,7,5],
      [7,0,INF],
      [5,INF,0]
  ]
  ```

* 인접 리스트

  * `연결 리스트`의 자료 구조를 이용함
  * 파이썬의 경우 배열, 연결리스트의 기능이 List 자료형으로 구현됨

  ```python
  # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]
  
  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1,7))
  graph[0].append((2,5))
  
  # 노드 1에 연결된 노드 정보 저장(노드,거리)
  graph[1].append((0,7))
  
  # 노드 2에 연결된 노드 정보 저장(노드,거리)
  graph[2].append((0,5))
  ```

* 두 방식의 차이점

  * 노드 개수가 많을수록 인접 행렬의 메모리 낭비가 인접 리스트에 비해 심하다
  * 반면 노드의 연결 정보를 얻는 속도는 인접 행렬이 좀 더 빠르다
    * 인접 행렬은 평균적으로 1회를 검증하지만
    * 인접 리스트는 리스트 내 원소를 차례로 순회하여 찾기 때문

##### DFS 동작 과정

`1` 탐색 시작 노드를 스택에 삽입하고 방문 처리

`2-1`스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 

`2-2`만약 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄.

`3` `2`의 과정을 더 수행할 수 없을 때까지 [stack의 길이가 0이 될 때까지] 반복함

`단`, DFS는 순서와 상관없이 처리할 수 있지만, 보통 노드 번호가 낮은 순서부터 처리하는 것이 유리하기 때문에 이를 염두에 두고 구현하는 것이 좋음

##### DFS의 특징

* 스택 자료 구조에 기초한 알고리즘
* 탐색에 걸리는 시간은 O(N)
* 재귀 함수를 통해 간결한 구현이 가능함

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드(v)를 방문 처리
    visited[v] = True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드(i)를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
        
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```



#### BFS

> Breath First Search
>
> 너비 우선 탐색, 가까운 토드부터 탐색하는 알고리즘
>
> > cf) DFS는 최대한 멀리 있는 노드를 먼저 찾기

##### BFS 동작

> 선입 선출 방식의 큐 자료구조 이용

`1` 탐색 시작 노드를 큐에 삽입하고 방문 처리

`2` 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않는 노드를 모두 큐에 삽입

`3` `2`번의 과정을 더 수행할 수 없을 때까지(queue의 길이가 0) 반복

##### BFS 특징

* 큐 자료구조에 기초한 알고리즘
* 탐색 수행에 O(N) 시간이 소요
* `일반적인 경우 실제 수행 시간이 DFS보다 좋음`
  * 재귀 함수로 DFS를 구현하면 컴퓨터 시스템의 동작 특성상 실제 프로그램의 수행 시간이 느려질 수 있음
  * 따라서 스택 라이브러리를 이용해 시간 복잡도를 완화하는 태크닉이 필요함

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복(큐의 길이가 0일 때까지)
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end='')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

* N X M의 2차원 배열에 대한 탐색 문제는 각 좌표를 노드로 하는 그래프 문제로 생각하여 풀 수 있음

  * 3 X 3 형태 2차원 배열, 캐릭터의 위치 (1,1), 상하좌우 움직임이 가능한 경우

    | (1,1) | (1,2) | (1,3) |
    | ----- | ----- | ----- |
    | (2,1) | (2,2) | (2,3) |
    | (3,1) | (3,2) | (3,3) |

    * 1,1에 대한 인접 리스트: 1,2 / 2,1
    * 2,2에 대한 인접 리스트: 1,2 / 2,1 / 2,3 / 3,2/

  * 매트릭스를 인접 리스트처럼 생각해서 연결된 좌표를 넣는 것인가..?



## 실전문제 3 음료수 얼려 먹기

N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

| 0    | 0    | 1    | 1    | 0    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | 0    | 0    | 1    | 1    |
| 1    | 1    | 1    | 1    | 1    |
| 0    | 0    | 0    | 0    | 0    |

```
#3개

00110
00011
11111
00000
```

`입력 조건`

* 첫 번째 줄에 얼음 틀의 새로 길이 N과 가로 길이 M이 주어진다. 
  * 1<= N,M <= 1,000
* 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
* 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

`출력 조건`

* 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

`입력 예시`

```
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
```

`출력 예시`

```
8
```

###### 문제 해설

* DFS로 해결할 수 있는 문제

* 그래프 형태의 모델링이 가능함

  `1` 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0' 이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문

  `2` 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있음

  `3` `1` ~ `2`번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다

* 소스코드

  ```python
  # N,M을 공백으로 구분하여 입력받기
  n,m = map(int,input().split())
  
  # 2차원 리스트의 맵 정보 입력받기
  graph = []
  for i in range(n):
      graph.append(list(map(int,input())))
      
  # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
  def dfs(x,y):
      # 주어진 범위를 벗어나는 경우에는 즉시 종료
      if x <= -1 or x >= n or y <= -1 or y >= m:
          return False
      # 현재 노드를 아직 방문하지 않았다면
      if graph[x][y] == 0:
          # 해당 노드 방문 처리
          graph[x][y] = 1
          # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
          dfs(x-1,y)
          dfs(x,y-1)
          dfs(x+1,y)
          dfs(x,y+1)
          return True
      return False
  
  # 모든 노드(위치)에 대하여 음료수 채우기
  result = 0
  for i in range(n):
      for j in range(m):
          # 현재 위치에서 DFS수행
          if dfs(i,j) == True:
              result += 1
              
  print(result) #정답
  ```

* My 코드

  ```python
  N,M = 15, 14
  tray = [list(map(int,input())) for _ in range(N)]
  visited = [[0]*M for _ in range(N)]
  
  dr = [-1,0,1,0]
  dc = [0,1,0,-1]
  
  def check(x,y):
      if x<0 or x == N: return False
      if y<0 or y == M: return False
      if tray[x][y] == 1: return False
      if visited[x][y] == 1: return False
      return True
  
  def dfs(v):
      r = v[0]; c=v[1]
      visited[r][c] = 1
      for i in range(4):
          nr = r + dr[i]; nc = c + dc[i]
          if check(nr,nc):
              dfs([nr,nc])
  
  cnt = 0
  for r in range(N):
      for c in range(M):
          if not tray[r][c] and not visited[r][c]:
              dfs([r,c])
              cnt += 1
  print(cnt)
  ```



## 실전문제 4 미로 탈출

동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

`입력 조건`

* 첫째 줄에 두 정수 N,M이 주어집니다. 
  * (4<=N,M<=200)
* 다음 N 개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
  * 각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
* 또한 시작 칸과 마지막 칸은 항상 1이다.

`출력 조건`

* 첫째 줄에 최소 이동 칸의 개수를 출력한다.

`입력 예시`

```
5 6
101010
111111
000001
111111
111111
```

`출력 예시`

```
10
```

###### 문제 해설

* BFS 문제
* 특정 노드 방문 시 그 이전 노드의 거리에 +1을 더하여 리스트에 넣기
* 단, 제시되는 소스 코드의 경우 미로의 탈출 방법이 단순하기 때문에 동작하며 보다 복잡한 경우에 대해서는 loop에 빠질 수 있음

* 소스 코드

  ```python
  from collections import deque
  
  # N,M을 공백으로 구분하여 입력받기
  n,m = map(int,input().split())
  # 2차원 리스트의 맵 정보 입력받기
  graph = []
  for i in range(n):
      graph.append(list(map(int,input())))
      
  # 이동할 네 방향 정의 [상,하,좌,우]
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  
  # BFS 소스코드 구현
  def bfs(x,y):
      # 큐(Queue)구현을 위해 deque 라이브러리 사용
      queue = deque()
      queue.append((x,y))
      # 큐가 빌 때까지 반복
      while queue:
          x,y = queue.popleft()
          # 현재 위치에서 네 방향으로의 위치 확인
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              # 미로 찾기 공간을 벗어난 경우 무시
              if nx < 0 or ny < 0 or nx >= n or ny >= m:
                  continue
              # 벽인 경우 무시
              if graph[nx][ny] == 0:
                  continue
              # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
              if graph[nx][ny] == 1:
                  graph[nx][ny] = graph[x][y] + 1
                  queue.append((nx,ny))
      # 가장 오른쪽 아래까지의 최단 거리 반환
      return graph[n-1][m-1]
  
  # BFS 수행 결과 출력
  print(bfs(0,0))
  ```

* My 코드

  ```python
  from collections import deque
  
  N,M = 5,6
  maze = [list(map(int,input())) for _ in range(N)]
  visited = [[0]*M for _ in range(N)]
  
  # r,c = N,M 종료
  
  dr = [-1,0,1,0]
  dc = [0,1,0,-1]
  
  def check(x,y):
      if x < 0 or x == N: return False
      if y < 0 or y == M: return False
      if visited[x][y] != 0: return False
      if maze[x][y] == 0: return False
      return True
  
  def BFS(v):
      sr = v[0]; sc = v[1]
      Q = deque()
      Q.append([sr,sc])
      visited[sr][sc] = 1
      while len(Q):
          q = Q.popleft()
          r = q[0]; c = q[1]
          if (r, c) == (N - 1, M - 1):
              return visited[r][c]
          for i in range(4):
              nr = r + dr[i]
              nc = c + dc[i]
              if check(nr,nc):
                  Q.append([nr,nc])
                  visited[nr][nc] = visited[r][c] + 1
  
  print(BFS((0,0)))
  ```

  