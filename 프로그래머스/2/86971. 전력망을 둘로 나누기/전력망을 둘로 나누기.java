class Solution {
    private boolean[][] graph;
    private boolean[] visited;
    
    public int solution(int n, int[][] wires) {
        graph = new boolean[n+1][n+1];
        int answer = n;
        
        // 전선 연결
        for (int[] wire : wires){
            int a = wire[0];
            int b = wire[1];
            
            graph[a][b] = true;
            graph[b][a] = true;
        }
        
        // 하나씩 끊어보기
        for (int[] wire : wires){
            int a = wire[0];
            int b = wire[1];
            
            graph[a][b] = false;
            graph[b][a] = false;
            
            visited = new boolean[n+1];
            
            int count = dfs(1, n);
            int other = n - count;
            int difference = Math.abs(count - other);
            
            answer = Math.min(answer, difference);
            
            graph[a][b] = true;
            graph[b][a] = true;
        }
        
        return answer;
    }
    
    private int dfs(int current, int n){
        visited[current] = true;
        int count = 1;
        
        for (int next = 1; next <= n; next++){
            if (graph[current][next] && !visited[next]){
                count += dfs(next, n);
            }
        }
        
        return count;
    }
}