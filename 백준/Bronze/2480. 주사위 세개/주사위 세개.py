dice = list(map(int, input().split()))

for num in dice:
    if dice.count(num) == 3:
        print(10000 + num * 1000)
        break
    elif dice.count(num) == 2:
        print(1000 + num * 100)
        break
else:
    print(max(dice) * 100)
