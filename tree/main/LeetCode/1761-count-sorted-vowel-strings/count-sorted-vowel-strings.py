import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # nCr 조합인데 한 세트 더?
        return math.comb(n + 4, 4)