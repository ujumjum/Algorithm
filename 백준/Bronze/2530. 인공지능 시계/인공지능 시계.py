h, m, s = map(int, input().split())
time = int(input())
    
total_s = (h * 3600) + (m*60) + s + time

new_h = (total_s // 3600) % 24
new_m = (total_s % 3600) // 60
new_s = total_s % 60
    
print(new_h, new_m, new_s)