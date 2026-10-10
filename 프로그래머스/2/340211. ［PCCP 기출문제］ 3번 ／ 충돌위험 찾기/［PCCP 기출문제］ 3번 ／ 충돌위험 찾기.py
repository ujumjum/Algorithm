def solution(points, routes):
    answer = 0
    robot_paths = []
    
    # 각 로봇의 시간별 이동 경로
    for route in routes:
        path = []
        
        # 첫 시작점
        r, c = points[route[0] -1]
        path.append((r, c))
        
        # 다음 포인트들을 순서대로 방문
        for i in range(1, len(route)):
            target_r, target_c = points[route[i] -1]
            
            # r 먼저
            while r != target_r:
                if r < target_r:
                    r += 1
                else: 
                    r -= 1
                
                path.append((r, c))
                
            while c != target_c:
                if c < target_c:
                    c += 1
                else:
                    c -= 1
                
                path.append((r, c))
        
        robot_paths.append(path)
    
    # 가장 오래 움직이는 로봇의 시간
    max_time = max(len(path) for path in robot_paths)
    
    # 같은 시간에 같은 좌표에 있는 로봇 개수 확인
    for time in range(max_time):
        position_count = {}
        
        for path in robot_paths:
            if time < len(path):
                pos = path[time]
                position_count[pos] = position_count.get(pos, 0) + 1
                
        # 같은 좌표에 2대 이상 있으면 emergency 1회
        for count in position_count.values():
            if count >= 2:
                answer += 1
            
    return answer