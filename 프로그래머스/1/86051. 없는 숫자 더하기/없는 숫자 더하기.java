class Solution {
    public int solution(int[] numbers) {
        // 0부터 9까지 합 = 45 -> 45-numbers의 합
        int answer = 45;
        
        for (int number : numbers){
            answer -= number;
        }
        return answer;
    }
}