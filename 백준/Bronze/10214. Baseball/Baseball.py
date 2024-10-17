t = int(input())

for _ in range(t):
    yon_score, ko_score =  0, 0
    
    for _ in range(9):
        yon, ko = map(int, input().split())
        yon_score += yon
        ko_score += ko
            
    if yon_score > ko_score:
        print("Yonsei")
    elif ko_score > yon_score:
        print("Korea")
    else:
        print("Draw")