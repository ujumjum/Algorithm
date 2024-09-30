# 스도쿠 - backtracking
# 같은 행, 열, 9칸 중복숫자 확인

# 1. 빈칸 찾기 (0)
# 2. backtracking : 1~9 차례로, 조건에 중복X
# 3. 유효 없다면, 다른 숫자 시도
# 4. 모든 빈칸 채우면 성공!

import sys
# 9x9 board
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]

# 빈칸 찾기
empty_spots = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

# 사용 여부를 기록하는 리스트
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

# 초기 상태에서 사용된 숫자들 기록
for i in range(9):
    for j in range(9):
        if board[i][j]:
            num = board[i][j]
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i // 3) * 3 + j // 3][num] = True

# backtracking
def backtracking(idx):
    if idx == len(empty_spots):
        for row in board:
            print(''.join(map(str, row)))
        sys.exit(0)

    x, y = empty_spots[idx]
    box_idx = (x // 3) * 3 + y // 3

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box_idx][num]:
            board[x][y] = num
            row_used[x][num], col_used[y][num], box_used[box_idx][num] = True, True, True
            backtracking(idx + 1)
            board[x][y] = 0
            row_used[x][num], col_used[y][num], box_used[box_idx][num] = False, False, False

backtracking(0)