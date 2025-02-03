def solution(strs, t):
    INF = float('inf')
    n = len(t)
    word_set = set(strs)
    
    dp = [INF] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for j in range(max(0, i-5), i):
            if t[j:i] in word_set:
                dp[i] = min(dp[i], dp[j] + 1)
                
    return dp[n] if dp[n] != INF else -1