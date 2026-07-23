class Solution {
    public int solution(int storey) {
        int stones = 0;
        
        while (storey > 0) {
            int digit = storey % 10;
            int nextDigit = (storey / 10) % 10;
            
            if (digit > 5 || (digit == 5 && nextDigit >= 5)){
                stones += 10 - digit;
                storey += 10;
            } else {
                stones += digit;
            }
            
            storey /= 10;
            
        }
        return stones;
    }
}