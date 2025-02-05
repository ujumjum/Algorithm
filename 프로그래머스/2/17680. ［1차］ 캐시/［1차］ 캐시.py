from collections import deque

def solution(cacheSize, cities):
    # 캐시 크기에 따른 실행시간 측정
    # LRU / hit : 1, miss : 5
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()
    total_time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            # Cache Hit
            cache.remove(city)
            cache.append(city)
            total_time += 1
        else:
            # Cache Miss
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            total_time += 5
                
    return total_time