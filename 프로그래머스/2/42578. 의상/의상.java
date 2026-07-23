import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> countByType = new HashMap<>();
        
        for (String[] cloth : clothes){
            String type = cloth[1];
            
            countByType.put(type, countByType.getOrDefault(type, 0) +1);
        }
        
        int answer = 1;
        
        for (int count : countByType.values()){
            answer *= count + 1;
        }
        
        // 모든 종류의 옷을 입지 않는 경우
        return answer - 1;
    }
}