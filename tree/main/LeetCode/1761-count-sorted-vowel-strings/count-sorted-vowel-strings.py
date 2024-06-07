class Solution:
    def countVowelStrings(self, n: int) -> int:
        # nCr 조합인데 한 세트 더?
        # (a, e, i, o, u)
        vowels = 5
        
        dic = [[0] * vowels for _ in range(n+1)]
        
        for j in range(vowels):
            dic[1][j] = 1
            
        
        for i in range(2, n+1):
            for j in range(vowels):
                dic[i][j] = sum(dic[i-1][k] for k in range(j+1))
                
        
        return sum(dic[n])