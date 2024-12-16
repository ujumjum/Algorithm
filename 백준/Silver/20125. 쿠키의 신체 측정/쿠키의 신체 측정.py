N = int(input())  # 판의 크기 N
grid = [input().strip() for _ in range(N)]  # 판의 상태를 입력받음

# 심장의 위치를 찾는 함수
def find_heart():
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 심장은 3x3 영역의 가운데에 있다.
            if grid[i][j] == '*' and grid[i-1][j] == '*' and grid[i+1][j] == '*' and grid[i][j-1] == '*' and grid[i][j+1] == '*':
                return i, j  # 0-based index로 반환

# 왼쪽 팔의 길이를 계산하는 함수
def arm_left(x, y):
    count = 0
    while y > 0 and grid[x][y-1] == '*':
        count += 1
        y -= 1
    return count

# 오른쪽 팔의 길이를 계산하는 함수
def arm_right(x, y):
    count = 0
    while y < N - 1 and grid[x][y+1] == '*':
        count += 1
        y += 1
    return count

# 허리의 길이를 계산하는 함수
def waist(x, y):
    count = 0
    while x < N - 1 and grid[x+1][y] == '*':
        count += 1
        x += 1
    return count

# 다리의 길이를 계산하는 함수
def leg(x, y):
    count = 0
    while x < N - 1 and grid[x+1][y] == '*':
        count += 1
        x += 1
    return count

# 심장의 위치를 찾음 (0-based index)
heart_x, heart_y = find_heart()

# 팔, 허리, 다리 길이 계산
left_arm = arm_left(heart_x, heart_y)
right_arm = arm_right(heart_x, heart_y)
waist_length = waist(heart_x, heart_y)
left_leg = leg(heart_x + waist_length, heart_y - 1)  # 허리 왼쪽 아래
right_leg = leg(heart_x + waist_length, heart_y + 1)  # 허리 오른쪽 아래

# 심장 위치 출력 (1-based index로 변환하여 출력)
print(heart_x + 1, heart_y + 1)
# 신체 부위 길이 출력
print(left_arm, right_arm, waist_length, left_leg, right_leg)