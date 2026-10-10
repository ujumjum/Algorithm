def solution(mats, park):
    # 큰돗자리부터 확인 - 처음성공한 크기가 정답
    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    for size in mats:
        # size x size 가능한 모든 시작점 탐색
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                can_place = True
                
                for x in range(i, i+size):
                    for y in range(j, j+size):
                        if park[x][y] != "-1":
                            can_place = False
                            break
                    
                    if not can_place:
                        break
                        
                if can_place: return size
    return -1