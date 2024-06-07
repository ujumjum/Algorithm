class Solution:
    def countVowelStrings(self, n: int) -> int:
        # nCr 조합인데 한 세트 더?
        # (a, e, i, o, u)
        vowels = 5
        
        # DP Bottom-up 방식
        tab = [[0] * vowels for _ in range(n+1)]
        
        # 길이 1이라면 1개씩
        for j in range(vowels):
            tab[1][j] = 1
            
        # DP 테이블 채우기
        for i in range(2, n+1):
            for j in range(vowels):
                tab[i][j] = sum(tab[i-1][k] for k in range(j+1))
                
        
        return sum(tab[n])