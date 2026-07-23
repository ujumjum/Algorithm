import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int work : works){
            queue.add(work);
        }
        
        while (n > 0 && !queue.isEmpty()){
            int maxWork = queue.poll();
            
            if (maxWork == 0){
                break;
            }
            
            queue.add(maxWork-1);
            n--;
        }
        
        long tired = 0;
        
        while (!queue.isEmpty()){
            long work = queue.poll();
            tired += work * work;
        }
        
        return tired;
    }
}