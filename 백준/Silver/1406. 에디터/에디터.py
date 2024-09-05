# 영소문자만 기록 가능 최대 600000
# 커서(맨앞, 맨뒤, 임의의 곳) : 길이 L이라면 L+1가지 위치 경우의수
# 명령어 : L, D, B, P $ 
import sys
input = sys.stdin.read

# 1. 입력 : 클럽장님처럼
data = input().splitlines()
s = list(data[0])
m = int(data[1])

# cursor 왼쪽부분
left_stack = s
# cursor 오른쪽 부분
right_stack = []

# 2. commands 처리
for i in range(2, 2+m):
    command = data[i]

    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:  # 제거
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[2])

# 3. 출력 : 최종 문자열
print(''.join(left_stack + list(reversed(right_stack))))