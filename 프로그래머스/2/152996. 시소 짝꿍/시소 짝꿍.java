import java.util.*;

class Solution {
    public long solution(int[] weights) {
        Arrays.sort(weights);
        
        Map<Integer, Integer> map = new HashMap<>();
        long answer = 0;
        
        for (int weight : weights){
            // 같은 몸무게
            answer += map.getOrDefault(weight, 0);
            
            // 이전 몸무게 : 현재 몸무게 = 2 : 3
            if (weight % 3 == 0){
                int partner = weight * 2 / 3;
                answer += map.getOrDefault(partner, 0);
            }
            
            // 1 : 2
            if (weight % 2 == 0){
                int partner = weight / 2;
                answer += map.getOrDefault(partner,0);
            }
            
            // 3 : 4
            if (weight % 4 == 0){
                int partner = weight *3 / 4;
                answer += map.getOrDefault(partner, 0);
            }
            
            map.put(weight, map.getOrDefault(weight, 0) + 1);
        }
        return answer;
    }
}