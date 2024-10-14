# 시작시각 - 필요한 시간 (분단위) => 끝나는 시각
h, m = map(int, input().split())
time = int(input())

total_m = m + time
new_h = h + (total_m // 60)
new_m = total_m % 60

new_h = new_h % 24

print(new_h, new_m)