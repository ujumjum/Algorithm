import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        less_spicy = heapq.heappop(scoville)
        second_less_spicy = heapq.heappop(scoville)
        
        new_scoville = less_spicy + (second_less_spicy * 2)
        
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
        
    return answer