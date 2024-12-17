def solution(sales, links):
    N = len(sales)  # 직원 수

    # 트리 구조
    graph = [[] for _ in range(N)]

    # links[팀장, 직원]을 통해 트리 구조 생성
    for a, b in links:
        graph[a - 1].append(b - 1)

    # dp[node][0]: node가 참석하지 않는 경우의 최소 매출액
    # dp[node][1]: node가 참석하는 경우의 최소 매출액
    dp = [[0, 0] for _ in range(N)]

    def dfs(node):
        if not graph[node]:  # 리프 노드인 경우
            dp[node][0] = 0  # 참석하지 않음
            dp[node][1] = sales[node]  # 참석함
            return
        
        sum_child = 0
        for child in graph[node]:
            dfs(child)
            sum_child += min(dp[child][0], dp[child][1])  # 자식 중 최소값 선택

        dp[node][1] = sum_child + sales[node]  # 현재 노드 참석
        
        # 자식 중 최소한 한 명이 참석해야 하는 경우
        if any(dp[child][0] > dp[child][1] for child in graph[node]):
            dp[node][0] = sum_child  # 자식들이 참석하는 경우
        else:
            dp[node][0] = sum_child + min(
                (dp[child][1] - dp[child][0] for child in graph[node]),
                default=0
            )  # 최소한 한 명 참석 보장

    dfs(0)  # CEO인 1번 직원부터 시작
    return min(dp[0][0], dp[0][1])  # CEO가 참석하는 경우와 참석하지 않는 경우 중 최소값
