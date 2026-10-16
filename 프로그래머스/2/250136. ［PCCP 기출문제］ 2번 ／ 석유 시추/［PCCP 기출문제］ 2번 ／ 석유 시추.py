from collections import deque

def solution(land):
    # 인접 lands 사이즈
    # col 별로 찍었을 때 최대 oil_by_col => 최종 max(oil_by_oil)
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for _ in range(n)]
    oil_by_col = [0] * m
    directions = [(-1, 0), (1,0), (0, -1), (0,1)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                
                oil_size = 1
                columns = {j}
                
                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
                        
                        if (0<=nx<n and 0<=ny<m
                           and land[nx][ny] == 1
                           and not visited[nx][ny]):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            oil_size += 1
                            columns.add(ny)
                for col in columns:
                    oil_by_col[col] += oil_size
    
    return max(oil_by_col)