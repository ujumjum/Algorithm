from collections import deque

def solution(n, results):
    # 그래프 초기화
    wins = [[] for _ in range(n)]
    losses = [[] for _ in range(n)]
    
    # 경기 결과 기록
    for a, b in results:
        wins[a-1].append(b-1)
        losses[b-1].append(a-1)
    
    def bfs(graph, start):
        visited = [False] * n
        queue = deque([start])
        visited[start] = True
        count = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        
        return count
    
    answer = 0
    for i in range(n):
        win_count = bfs(wins, i)
        lose_count = bfs(losses, i)
        
        if win_count + lose_count == n - 1:
            answer += 1
    
    return answer