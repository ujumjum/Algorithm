h, m = map(int, input().split())

if m < 45:
    h = (h-1) % 24
    m = m + 60 -45
else: 
    m -= 45
    
print(h, m)