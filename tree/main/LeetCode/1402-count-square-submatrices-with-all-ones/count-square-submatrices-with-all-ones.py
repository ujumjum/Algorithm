class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # 1로 정사각형 만들 수 있는 최대 개수 구하기
        # side 1 인거부터 주위에 만들 수 있는 정사각형있나 살피기(왼, 위, 왼대각) : dp에 개수 저장
        rows, cols = len(matrix), len(matrix[0])
        
        # 각 셀에서 끝나는 정사각형 부분 행렬의 최대 크기를 저장
        # dp = [[0]*cols for _ in range(rows)]
        dp = []
        for _ in range(rows):
            row = [0] * cols
            dp.append(row)
        
        max_squares = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # 첫번째 행 or 첫번째 열
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    # 왼쪽, 위쪽, 왼쪽 위 대각선 최소값에 + 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_squares += dp[i][j]
                
        return max_squares