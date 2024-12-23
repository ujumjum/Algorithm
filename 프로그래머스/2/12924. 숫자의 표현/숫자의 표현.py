def solution(n):
    cnt = 0
    
    for start in range(1, n+1):
        total = 0
        for num in range(start, n+1):
            total += num
            if total == n:
                cnt += 1
                break
            elif total > n:
                break
    return cnt