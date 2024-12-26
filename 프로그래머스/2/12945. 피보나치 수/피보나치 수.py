def solution(n):
    # 0과 1을 제외한 수는 모두 0으로 시작
    dp = [0] * (n + 1)
    dp[1] = 1  # 피보나치 수 첫 번째 값

    # 2부터 n까지 반복하여 피보나치 수 계산
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    return dp[n]