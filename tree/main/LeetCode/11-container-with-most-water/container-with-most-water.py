class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 가장 많은 물을 담을 수 있는 컨테이너 만들기
        # max_area : w*h 
        
        # 1. left and right 끝과 끝에서 좁히기
        left = 0
        right = len(height)-1
        max_area = 0
        
        # 2. 최대 면적 구하기
        while left<right:
            # 너비
            w = right-left
            
            # 높이 : 더 낮은쪽
            h = min(height[left], height[right])
            
            # 면적
            area = w * h
            max_area = max(max_area, area)
            
            #3.  Greedy 일단 낮은 쪽을 버림(이동)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        