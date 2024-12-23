def solution(n):
    battery = 0
    
    while n > 0:
        # 1. k 칸 점프(k만큼 건전지)
        if n % 2 == 1:
            battery += 1
        # 2. 순간이동 : 현재까지 거리 * 2
        n //= 2
        
    # N 까지 이동하기 위한 최소 건전지
    return battery