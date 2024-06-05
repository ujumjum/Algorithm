class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal_cnt = 0
        balance = 0
        
        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1
        
            if balance == 0:
                bal_cnt += 1
        
        return bal_cnt