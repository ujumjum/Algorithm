class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        origin_arr = [0] * len(pref)
        
        origin_arr[0] = pref[0]
        
        for i in range(1, len(pref)):
            origin_arr[i] = pref[i] ^ pref[i-1]
            
        return origin_arr