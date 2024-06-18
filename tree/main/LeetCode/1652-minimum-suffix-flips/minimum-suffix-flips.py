class Solution:
    def minFlips(self, target: str) -> int:
        flip_cnt = 0
        s = '0'  # 초기 상태는 '0'

        for char in target:
            if char != s:
                flip_cnt += 1
                s = char  # 현재 상태를 target의 현재 비트로 업데이트
        
        return flip_cnt