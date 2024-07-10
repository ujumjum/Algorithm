class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 왼쪽, 왼쪽 대각선, 위쪽 모두 1 이어야 함
        
        # matrix size
        rows = len(matrix)
        cols = len(matrix[0])
        
        # dp
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_size = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_size = max(max_size, dp[r+1][c+1])
        
        return max_size * max_size