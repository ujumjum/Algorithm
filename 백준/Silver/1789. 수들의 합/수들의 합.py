s = int(input())

total = 0
cnt = 0

i = 1
while total + i <= s:
    total += i
    cnt += 1
    i +=1

print(cnt)