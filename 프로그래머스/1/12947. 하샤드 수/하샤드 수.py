def solution(x):
    n = len(str(x))
    total = 0
    
    for i in range(n):
        total += int(str(x)[i])
        
    answer = True if x % total == 0 else False
    
    return answer