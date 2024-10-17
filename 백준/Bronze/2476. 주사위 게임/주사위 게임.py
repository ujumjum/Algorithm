n = int(input())
max_prize = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        prize = 10000 + a * 1000
    elif a==b or b==c:
        prize = 1000 + b * 100
    elif a==c:
        prize = 1000 + a * 100
    else:
        prize = max(a,b,c) * 100
    
    if max_prize < prize:
        max_prize = prize
        
print(max_prize)