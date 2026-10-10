def solution(a, b):
    answer = 0
    n = len(a)
    
    for i in range(0, n):
        answer += a[i] * b[i]
            
    return answer