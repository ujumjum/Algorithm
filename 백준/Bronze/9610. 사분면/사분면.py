n = int(input())
counts = [0, 0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        counts[4] += 1
    elif x > 0 and y > 0:
        counts[0] += 1
    elif x < 0 and y > 0:
        counts[1] += 1
    elif x < 0 and y < 0:
        counts[2] += 1
    elif x > 0 and y < 0:
        counts[3] += 1

labels = ["Q1", "Q2", "Q3", "Q4", "AXIS"]
for i in range(5):
    print(f"{labels[i]}: {counts[i]}")
