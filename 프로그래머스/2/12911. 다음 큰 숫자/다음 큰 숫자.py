def solution(n):
    ones_cnt = bin(n).count('1')
    
    next_num = n + 1
    while bin(next_num).count('1') != ones_cnt:
        next_num += 1
        
    return next_num