def solution(n, times):
    # start initiate
    min_time = 1
    # worst case
    max_time = max(times) * n
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        # possible peple to pass during mid_time
        pass_people = 0
        for cur_time in times:
            pass_people += mid_time // cur_time
        
        if pass_people >= n:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
            
    return min_time