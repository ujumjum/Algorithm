def solution(elements):
    n = len(elements)
    elements += elements
    unique_sums = set()
    
    for length in range(1, n+1):
        unique_sums.update(sum(elements[i:i+length]) for i in range(n))
            
    return len(unique_sums)