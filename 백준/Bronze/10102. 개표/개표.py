v = int(input())
votes = input().strip()

cnt_a = votes.count('A')
cnt_b = votes.count('B')

print("A" if cnt_a > cnt_b else "B" if cnt_b > cnt_a else "Tie")