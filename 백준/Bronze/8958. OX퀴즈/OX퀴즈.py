t = int(input())

for _ in range(t):
    result = input().strip()
    score = 0
    seq = 0
    
    for char in result:
        if char == 'O':
            seq += 1
            score += seq
        else:
            seq = 0
            
    print(score)