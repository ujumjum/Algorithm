def solution(a): 
    result = [False] * len(a) 
    min_front = float('inf') 
    min_back = float('inf') 
    
    # 앞, 뒤 동시에 최소 값이 갱신되는 지점을 저장해둔다. 
    # 갱신 지점들의 개수가 answer가 된다. 
    for i in range(len(a)): 
        if a[i] < min_front: 
            min_front = a[i] 
            result[i] = True 
        if a[-1-i] < min_back: 
            min_back = a[-1-i] 
            result[-1-i] = True 
    
    return sum(result)