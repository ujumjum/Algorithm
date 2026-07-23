import java.util.*;

class Solution {
    private Set<String> combinations = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        boolean[] selected = new boolean[user_id.length];
        // 1. user_id, banned_id match 되는거 찾기
        findCombinations(user_id, banned_id, selected, 0);
        // 2. 경우의 수 조합
        return combinations.size();
    }
    
    private void findCombinations(String[] users, String[] bannedUsers, boolean[] selected, int bannedIndex){
        // 모든 불량 사용자 패턴에 사용자를 배정한 경우
        if (bannedIndex == bannedUsers.length){
            saveCombination(selected);
            return;
        }
        
        // 현재 불량 사용자 패턴과 일치하는 사용자 찾기
        for (int userIndex = 0; userIndex < users.length; userIndex++){
            if (selected[userIndex]){
                continue;
            }
            
            if (!isMatch(users[userIndex], bannedUsers[bannedIndex])){
                continue;
            }
            
            selected[userIndex] = true;
            
            findCombinations(users, bannedUsers, selected, bannedIndex+1);
            
            selected[userIndex] = false;
        }
    }
    
    private boolean isMatch(String user, String bannedUser){
        if (user.length() != bannedUser.length()){
            return false;
        }
        
        for (int i = 0; i < user.length(); i++){
            if (bannedUser.charAt(i) == '*'){
                continue;
            }
            if (user.charAt(i) != bannedUser.charAt(i)){
                return false;
            }
        }
        
        return true;
    }
    
    private void saveCombination(boolean[] selected) {
        StringBuilder combination = new StringBuilder();
        
        for (int i = 0; i< selected.length; i++){
            if (selected[i]){
                combination.append(i).append(",");
            }
        }
        
        combinations.add(combination.toString());
    }
}