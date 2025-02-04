def solution(tickets):
    graph = {}
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
        
    for key in graph.keys():
        graph[key].sort()
        
    route = []
    
    def dfs(airport):
        while airport in graph and graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        route.append(airport)
        
    dfs("ICN")
    
    return route[::-1]  # 역순 출력