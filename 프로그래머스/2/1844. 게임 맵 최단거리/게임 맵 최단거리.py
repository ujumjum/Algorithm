from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return cnt
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if (0<=nx<n and 0<=ny<m
               and maps[nx][ny]==1
               and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    
    return -1