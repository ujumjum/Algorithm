class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int start = 1;
        int range = 2 * w + 1;
        
        for (int station : stations){
            // 전파 시작
            int signalStart = station - w;
            // 전파 닿지 않는 구간 길이
            int length = signalStart - start; 
            
            if (length > 0){
                answer += length / range;
                
                if (length % range != 0){
                    answer++;
                }
            }
            // 다음 위치로 이동
            start = station + w + 1;
        }
        
        if (start <= n){
            int length = n - start + 1;
            answer += length / range;
            if(length % range != 0){
                answer++;
            }
        }
        
        return answer;
    }
}