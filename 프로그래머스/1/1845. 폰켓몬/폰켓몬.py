def solution(nums):
    unique_ponketmons = set(nums)
    
    max_select = len(nums) // 2
    
    return min(len(unique_ponketmons), max_select)