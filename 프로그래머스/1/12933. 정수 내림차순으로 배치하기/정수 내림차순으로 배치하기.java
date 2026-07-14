import java.util.Arrays;

class Solution {
    public long solution(long n) {
        char[] digits = String.valueOf(n).toCharArray();
        
        Arrays.sort(digits);
        StringBuilder answer = new StringBuilder();
        
        for (int i = digits.length - 1; i >= 0; i--){
            answer.append(digits[i]);
        }
        
        return Long.parseLong(answer.toString());
    }
}