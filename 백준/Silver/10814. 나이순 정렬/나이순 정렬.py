n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

sorted_members = sorted(members, key=lambda member : member[0])
# sorted_members = merge_sort(members)

for member in sorted_members:
    print(member[0], member[1])