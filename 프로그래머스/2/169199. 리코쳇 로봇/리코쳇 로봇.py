from collections import deque

def solution(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(board)
    m = len(board[0])
    
    # R 찾기
    start = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
    
    # BFS
    queue = deque()
    queue.append((start[0], start[1], 0))
    
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        # 도착!
        if board[x][y] == 'G':
            return moves
        
        for dx, dy in directions:
            nx = x
            ny = y
            
            while (0<=nx+dx<n and 0<=ny+dy<m
                   and board[nx+dx][ny+dy] != 'D'):
                nx += dx
                ny += dy
                
            # 한칸도 못움직였다면 다른 방향 ㄱㄱ
            if nx == x and ny == y:
                continue
            
            if not visited[nx][ny]:
                visited[nx][ny] =True
                queue.append((nx, ny, moves+1))
                 
    return -1