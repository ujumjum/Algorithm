# DFS, BFS 탐색 결과 출력
# 정점 번호가 작은 것 먼저 방문 (1~n)
import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.read

# DFS - 재귀
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS - queue
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


# input
data = input().splitlines()
n, m, v = map(int, data[0].split())
graph = [[] for _ in range(n+1)]

# 간선
for line in data[1:m+1]:
    a, b = map(int, line.split())
    graph[a].append(b)
    graph[b].append(a)

# 번호 작은것부터 방문
for i in range(1, n+1):
    graph[i].sort()

# DFS
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

# BFS
visited = [False] * (n+1)
bfs(graph, v, visited)
print()
