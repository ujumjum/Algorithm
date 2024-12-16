from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    # 상, 하, 좌, 우 방향
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # BFS 큐 초기화 시작점(0,0) 거리 1
    queue = deque([(0,0,1)])
    # 방문한 곳 marking
    visited = set((0,0))
    
    # queue 빌 때까지
    while queue:
        # 현재 위치, 거리 꺼냄
        x, y, dist = queue.popleft()
        
        # 목표지점 (N-1, M-1) 도착!
        if x == N -1 and y == M -1:
            return dist
        
        # 상하좌우로 이동
        for dx, dy in directions:
            # 새로운 위치
            nx, ny = x + dx, y + dy
            # 맵 범위 내 && no 벽 && not visited
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and (nx, ny) not in visited:
                # 새 위치, 거리 추가
                queue.append((nx, ny, dist+1))
                # 방문 marking
                visited.add((nx, ny))
    
    return -1