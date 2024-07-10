class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle is None:
            return None
        
        #Top-Down
        # 아래, 오른쪽아래 중 작은 값 선택해서 path 찾기
        memo = {}
        
        def dfs(row, col):
            # Base case : 마지막 행
            if row == len(triangle) -1:
                return triangle[row][col]
        
            if (row, col) in memo:
                return memo[(row,col)]
            
        
            bottom = dfs(row+1, col)
            right_bottom = dfs(row+1, col+1)
            memo[(row, col)] = triangle[row][col] + min(bottom, right_bottom)
            
            return memo[(row, col)]
        
        return dfs(0,0)
    
    
        # Bottom-UP
        # 맨 아래~위로 올라가면서 triangle에 값 갱신
        # 공간 사용 줄임 + 효율성
#         if not triangle:
#             return 0
        
#         # 아래에서부터 위로 계산
#         # 아래에서 2번째 행 - 역순으로
#         for row in range(len(triangle) - 2, -1, -1):
#             for col in range(len(triangle[row])):
#                 # 현재 요소를 아래 두 요소 중 더 작은 값과 합하여 갱신
#                 triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
#         # 맨 위의 요소가 최소 경로 합을 가지게 됨
#         return triangle[0][0]