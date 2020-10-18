# deque 사용하기
from collections import deque

# input값 받기
N, M, K, X = map(int,input().split())
tmp = [list(map(int,input().split())) for _ in range(M)]

# 그래프 인접 리스트로 그리기
G = [[] for _ in range(N+1)]

# 방문 체크하기
visit = [0]*(N+1)
for i in range(M):
    f,t = tmp[i][0], tmp[i][1]
    G[f].append(t)

# 정답 리스트
answer = []

# BFS 순회 ,while 방식, 도달해야 하는 거리 K +1
def bfs(s):
    q = deque()
    q.append(s)
    visit[s] = 1
    while len(q):
        v = q.popleft()
        if visit[v] == K+1:
            answer.append(v)
        elif visit[v] > K+1:
            return
        for w in G[v]:
            if not visit[w]:
                q.append(w)
                visit[w] = visit[v] + 1
# 시작점 = X
bfs(X)
# 원소가 없으면 -1, 아니면 순서대로 출력
if not len(answer):
    print(-1)
else:
    for ans in answer:
        print(ans)

'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
'''
4 3 2 1
1 2 
1 3
1 4
'''
'''
4 4 1 1
1 2
1 3
2 3
2 4
'''