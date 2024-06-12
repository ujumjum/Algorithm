from collections import deque

def solution(n, edge):
    # 1번 노드에서 가장 멀리 떨어진 노드의 개수
    answer = 0
    
    # 1. 그래프 -> 인접 리스트로
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # 2. BFS 위한 큐, 거리 리스트 초기화
    distances = [-1] * (n + 1)
    distances[1] = 0 # 1번 노드
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1: # 방문하지 않은 노드
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    # 3. 가장 멀리 떨어진 노드 개수
    max_distance = max(distances)
    answer = distances.count(max_distance)
    
    return answer