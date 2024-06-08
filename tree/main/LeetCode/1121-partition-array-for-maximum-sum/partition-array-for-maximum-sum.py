class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # DP table 초기화
        tab = [0]* (n+1)
        
        for i in range(1, n+1):
            max_val = 0
            # tabulation
            for j in range(1, min(k,i) +1):
                max_val = max(max_val, arr[i-j])
                tab[i] = max(tab[i], tab[i-j] + max_val * j)
                
        return tab[n]