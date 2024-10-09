def solution(board):
    # 직선 : 100원, 코너 : 500원
    # 최소 비용
    N = len(board)
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    INF = float('inf')
    
    cost = [[[INF]*4 for _ in range(N)] for _ in range(N)]
    queue = []
    
    # 시작(0,0) 0원
    for i in range(4):
        cost[0][0][i] = 0
    queue.append((0,0,-1,0))    # 행, 열, 이전방향, 누적cost
    
    while queue:
        x, y, prev_dir, cur_cost = queue.pop(0)
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                # linear
                if prev_dir == -1 or prev_dir == i:
                    new_cost = cur_cost + 100
                # corner : 코너자체 500 + 새로운 직선 100
                else:
                    new_cost = cur_cost + 600
                    
                if new_cost < cost[nx][ny][i]:
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))
    
    return min(cost[N-1][N-1])