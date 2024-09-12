# 모든 연결된 집 봐야함 - 전체 탐색 DFS / BFS
def dfs(x, y):
    grid[x][y] = 0     # 집이 1 -> 0으로 방문처리
    cnt = 1             # 현재 위치 집 개수

    # 상하좌우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도 범위, no 방문
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
            cnt += dfs(nx, ny)  # 재귀적 DFS 탐색, 연결된 집 count

    return cnt          # 연결된 집 수

# input
N = int(input())
grid = [list(map(int, input())) for _ in range(N)]

house_cnt = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:     # 방문되지 않은 집
            house_cnt.append(dfs(i,j))  # 단지 내 집 수

# output
print(len(house_cnt))
for h in sorted(house_cnt):
    print(h)