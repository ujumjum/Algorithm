# 웜 바이러스, 양방향 그래프
# 출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
# 1번 컴퓨터 통해 바이러스 걸리는 컴퓨터 수, 1번은 no count
# BFS
from collections import deque

# 입력
N = int(input())
C = int(input())

# 인접행렬
coms = [[0] * (N+1) for _ in range(N+1)]

# 연결 정보
for _ in range(C):
    a, b = map(int, input().split())
    coms[a][b] = coms[b][a] = 1

visited = [False] * (N+1)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    # 1번에서 출발
    cnt = 0
    
    while queue:
        node = queue.popleft()
        for i in range(1, N+1):
            if coms[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt

worm_cnt = bfs(1)
print(worm_cnt)