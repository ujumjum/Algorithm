class Solution {
    public int solution(int sticker[]) {
        if (sticker.length==1) return sticker[0];
        
        int firstCase = getMaxScore(sticker, 0, sticker.length-2);
        int secondCase = getMaxScore(sticker, 1, sticker.length-1);
        
        return Math.max(firstCase, secondCase);
    }
    
    private int getMaxScore(int[] sticker, int start, int end){
        if (start == end) {
            return sticker[start];
        }
        
        int[] maxScores = new int[sticker.length]; 
        
        maxScores[start] = sticker[start];
        
        maxScores[start+1] = Math.max(sticker[start], sticker[start+1]);
        
        for (int i = start + 2; i <= end; i++){
            maxScores[i] = Math.max(maxScores[i-1], maxScores[i-2] + sticker[i]);
        }
        return maxScores[end];
    }
}