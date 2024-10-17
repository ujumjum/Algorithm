x_cnt = []
y_cnt = []

for _ in range(3):
    x, y = map(int, input().split())
    x_cnt.append(x)
    y_cnt.append(y)
    
x4 = 0
y4 = 0

for x in x_cnt:
    if x_cnt.count(x) == 1:
        x4 = x
for y in y_cnt:
    if y_cnt.count(y) == 1:
        y4 = y

print(x4, y4)