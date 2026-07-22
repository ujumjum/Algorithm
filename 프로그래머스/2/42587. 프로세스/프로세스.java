import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> queue = new ArrayDeque<>();
        
        for (int i = 0; i < priorities.length; i++){
            queue.offer(i);
        }
        
        int execute = 0;
        
        while (!queue.isEmpty()){
            int current = queue.poll();
            boolean hasHigherPriority = false;
            
            for (int i = 0; i < priorities.length; i++){
                if (priorities[current] < priorities[i]){
                    hasHigherPriority = true;
                    break;
                }
            }
            
            if (hasHigherPriority){
                queue.offer(current);
            } else {
                execute++;
                priorities[current] = 0;
                
                if (current == location){
                    return execute;
                }
            }
        }
        return execute;
    }
}