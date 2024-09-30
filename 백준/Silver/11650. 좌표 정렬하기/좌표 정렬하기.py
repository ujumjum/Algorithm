n = int(input())
spot = []

for _ in range(n):
    x, y = map(int, input().split())
    spot.append((x,y))

result = sorted(spot, key=lambda x : (x[0], x[1]))

for r in result:
    print(r[0], r[1])